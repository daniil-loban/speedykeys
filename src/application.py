from PySide6 import QtWidgets

from .managers.pluginManager import PluginManager
from .managers.settingsManager import SettingsManager 

class Application(QtWidgets.QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.settings = SettingsManager()
        self.pluginManager = PluginManager()

    def getSettings(self):
        return self.settings
    
    def registerPlugins(self, window):
        self.pluginManager.registerPlugin(window)
        self.pluginManager.plugins[0].name()

    def getPluginCount(self):
        return self.pluginManager.getPluginCount()

    def getPluginByIndex(self, index):
        return self.pluginManager.getPluginByIndex(index)