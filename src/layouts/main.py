import os
from sys import argv, exit
from pathlib import Path
from PySide6 import QtCore
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ..helpers import getAppSettings, registerPlugins
from .componets.customTextEdit import CustomTextEdit
from .settings import SettingsWindow
from ..managers.layoutManager import apply_ui

class Window(QMainWindow):
    def __init__(self, app=None):
        super(Window, self).__init__()
        self.app = app
        self.settings = getAppSettings()
        self.load_lang()        
        apply_ui(self, 'mainwindow.ui', [CustomTextEdit])
        self.update_text_styles()
        registerPlugins(self)
  
    def load_lang(self):
        translator = QtCore.QTranslator(self.app)
        path =  os.fspath(Path(__file__).resolve().parents[1] / 'lang' / f'{self.settings.get_language()}.qm' )
        if translator.load(path): self.app.installTranslator(translator)

    def update_text_styles(self):
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
           