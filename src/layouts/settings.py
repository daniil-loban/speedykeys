from PySide6 import QtCore
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ..helpers import Initer, center_widget, getAppInstance
from .componets.customTextEdit import CustomTextEdit
from ..managers.layoutManager import apply_ui


class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        apply_ui(self, 'settings.ui', [CustomTextEdit])
        app_instance = getAppInstance()
        with Initer(self) as i:
            center_widget(i)
            i.settings = app_instance.getSettings() #SettingsManager()
            i.set_ui_values()
            i.update()

    def set_ui_values(self):
        spin =  self.findChild(QSpinBox, "cursorWidth")
        if spin: spin.setValue(self.settings.get_text_cursor_width())
        self.set_languages()
       
        pl = self.settings.get_all_plugins()
        pluginList =  self.findChild(QListWidget, "pluginsList")
        pluginList.setDragDropMode(QAbstractItemView.InternalMove)
        for plugin in pl:
            qli = QListWidgetItem(plugin)
            qli.setFlags(qli.flags() | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsDragEnabled)
            qli.setCheckState(Qt.CheckState.Checked)
            pluginList.addItem(qli)

    def set_languages(self):
        comboBox =  self.findChild(QComboBox, "comboBox")
        languages = self.settings.get_all_languages()
        comboBox.addItems(languages)
        lang = self.settings.get_language()
        index = comboBox.findText(lang)
        if index != -1:
            comboBox.setCurrentIndex(index)        

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

    def updateColor(self, propetyName):
        getter = getattr(self.settings, f'get_{propetyName}')
        setter = getattr(self.settings, f'set_{propetyName}')
        color = self.get_color(getter())
        if (color):
            setter(color)
            self.update()

    @QtCore.Slot()
    def on_backgroundButton_clicked(self):
        self.updateColor('text_background_color')

    @QtCore.Slot()
    def on_textBeforeColorButton_clicked(self):
        self.updateColor('previous_text_color')

    @QtCore.Slot()
    def on_textCurrentColorButton_clicked(self):
        self.updateColor('current_text_color')

    @QtCore.Slot()
    def on_textAfterColorButton_clicked(self):
        self.updateColor('next_text_color')

    @QtCore.Slot(int)
    def on_cursorWidth_valueChanged(self, val):
        self.settings.set_text_cursor_width(val)
        self.update() 

    @QtCore.Slot()
    def on_buttonBox_accepted(self):
        self.settings.save()