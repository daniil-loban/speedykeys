from PySide6 import QtCore
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ..layouts.componets.customTextEdit import CustomTextEdit
from ..managers.settingsManager import SettingsManager
from ..managers.textManager import TextManager
from ..managers.layoutManager import apply_ui

class Initer():
    def __init__(self, o) -> None:
        self.o = o

    def __enter__(self):
        self.o.isInit = True
        return self.o
    
    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.o.isInit = False

class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        apply_ui(self, 'settings.ui', [CustomTextEdit])
        with Initer(self) as i:
            i.center_widget()
            i.settings = SettingsManager()
            i.set_ui_values()
            i.update()

    def set_ui_values(self):
        spin =  self.findChild(QSpinBox, "cursorWidth")
        if spin: spin.setValue(self.settings.get_text_cursor_width())
        self.set_languages()

    def set_languages(self):
        comboBox =  self.findChild(QComboBox, "comboBox")
        languages = self.settings.get_all_languages()
        comboBox.addItems(languages)
        lang = self.settings.get_language()
        index = comboBox.findText(lang)
        if index != -1:
            comboBox.setCurrentIndex(index)        

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
        if not self.isInit:
            self.settings.set_language(combo.currentText())

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