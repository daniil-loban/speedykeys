from sys import argv, exit
from PySide6 import QtCore
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ..layouts.componets.customTextEdit import CustomTextEdit
from ..layouts.settings import SettingsWindow
from ..managers.settingsManager import SettingsManager
from ..managers.layoutManager import apply_ui

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        apply_ui(self, 'mainwindow.ui', [CustomTextEdit])
        self.settings = SettingsManager()
        self.update_text_styles()
  
    def update_text_styles(self):
        self.settings.open()
        self.textedit = self.findChild(QTextEdit, u"textEdit")
        self.textEdit.stylize_textedit(self.settings)

    @QtCore.Slot()
    def on_actionOpen_triggered(self):
        pass

    @QtCore.Slot()
    def on_actionQuit_triggered(self):
        quit()

    @QtCore.Slot()
    def on_actionPreferences_triggered(self):
        s = SettingsWindow(self)
        isOk = s.exec()
        if isOk:
            self.update_text_styles()
           