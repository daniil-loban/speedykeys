from PySide6 import QtWidgets
from PySide6.QtGui import QGuiApplication

def getAppInstance():
    return QtWidgets.QApplication.instance()

def getAppSettings():
    return getAppInstance().getSettings()

def registerPlugins(window):
    return getAppInstance().registerPlugins(window)

def getPluginCount():
    return getAppInstance().getPluginCount()

def getPluginByIndex(index):
    return getAppInstance().getPluginByIndex(index)

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

class Initer():
    def __init__(self, o) -> None:
        self.o = o

    def __enter__(self):
        self.o.isInit = True
        return self.o
    
    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.o.isInit = False
