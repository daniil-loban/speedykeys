import os
from pathlib import Path
from PySide6 import QtCore, QtUiTools

class UiLoader(QtUiTools.QUiLoader):
    _baseinstance = None
    
    def createWidget(self, classname, parent=None, name=''):
        if parent is None and self._baseinstance is not None:
            widget = self._baseinstance
            return widget
        widget = super().createWidget(classname, parent, name)
        if self._baseinstance is not None:
            setattr(self._baseinstance, name, widget)
        return widget

    def loadUi(self, uifile, baseinstance=None):
        self._baseinstance = baseinstance
        widget = self.load(uifile)
        QtCore.QMetaObject.connectSlotsByName(baseinstance)
        return widget

def get_ui_path():
    return os.fspath(Path(__file__).resolve()
        .parents[1] / 'layouts' / 'ui')

def apply_ui(baseinstance, uifile, customwidgets = []):
    loader = UiLoader()
    path = Path(get_ui_path(), uifile)
    for widget in customwidgets:
        loader.registerCustomWidget(widget)
    loader.loadUi(path, baseinstance)