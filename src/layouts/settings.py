from PySide6 import QtCore
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ..layouts.componets.customTextEdit import CustomTextEdit
from ..managers.settingsManager import SettingsManager
from ..managers.textManager import TextManager
from ..managers.layoutManager import apply_ui


class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        apply_ui(self, 'settings.ui', [CustomTextEdit])
        self.center_widget()
        self.settings = SettingsManager()
        self.set_ui_values()
        self.update()

    def set_ui_values(self):
        spin =  self.findChild(QSpinBox, "cursorWidth")
        if spin: spin.setValue(self.settings.get_text_cursor_width())

    def center_widget(self):
        host = self.parentWidget()
        if host: 
            hostRect = host.geometry();
            self.move(hostRect.center() - self.rect().center())
        else:
            screenGeometry = QGuiApplication.screens()[0].geometry()
            x = (screenGeometry.width() - self.width()) / 2
            y = (screenGeometry.height() - self.height()) / 2
            self.move(x, y);

    def get_font(self):
        self.textedit = self.findChild(QTextEdit, u"textEdit")
        if not self.textedit: return
        b, font = QFontDialog.getFont(self.textedit.font())
        return (font.family() , f'{font.pointSize()}pt')

    def get_color(self, presetColor):
        dialog =QColorDialog(self)
        if presetColor.startswith('#'):
            color = QColor(presetColor)
        elif presetColor.startswith('rgb'): 
            r, g, b = map(int, self.settings.get_text_background_color()[4:-1].split(','))
            color = QColor(r, g, b)
        else:
            color = QColor(presetColor)
        result = dialog.getColor(color)
        return result.toRgb().name() if result.isValid() else None

    def update(self):
        self.textEdit.stylize_textedit(self.settings)
        self.setFocus()

    @QtCore.Slot()
    def on_tabWidget_currentChanged(self):
        pass

    @QtCore.Slot()
    def on_comboBox_currentIndexChanged(self):
        combo = self.findChild(QComboBox, "comboBox")
        #print(combo.currentText())

    @QtCore.Slot()
    def on_fontButton_clicked(self):
        fontFamily, fiontSize = self.get_font()
        self.settings.set_font(fontFamily, fiontSize)
        self.update()

    @QtCore.Slot()
    def on_backgroundButton_clicked(self):
        color = self.get_color(self.settings.get_text_background_color())
        if (color):
            self.settings.set_text_background_color(color)
            self.update()

    @QtCore.Slot()
    def on_textBeforeColorButton_clicked(self):
        color = self.get_color(self.settings.get_previous_text_color())
        if color:
            self.settings.set_previous_text_color(color)
            self.update() 

    @QtCore.Slot()
    def on_textCurrentColorButton_clicked(self):
        color = self.get_color(self.settings.get_current_text_color())
        if color:
            self.settings.set_current_text_color(color)
            self.update()

    @QtCore.Slot()
    def on_textAfterColorButton_clicked(self):
        color = self.get_color(self.settings.get_next_text_color())
        if color:
            self.settings.set_next_text_color(color)
            self.update() 

    @QtCore.Slot(int)
    def on_cursorWidth_valueChanged(self, val):
        self.settings.set_text_cursor_width(val)
        self.update() 

    @QtCore.Slot()
    def on_buttonBox_accepted(self):
        self.settings.save()