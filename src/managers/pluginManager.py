class PluginManager:
    def __init__(self) -> None:
        self.plugins = []

    def registerPlugin(self, window, pluginPath='/home/daniil/Desktop/SK/speedykeys/src/plugins/counter/plugin.py'):
        with open(pluginPath, 'r') as f:
            code = '    '.join(f.readlines())
            pluginContent =f'''
def getPlugingExtractor():
    {code}
    return Plugin
glob["getPlugingExtractor"]=getPlugingExtractor
'''
            glob = {}
            exec(pluginContent, {"glob": glob})
            pluginExtractor = glob["getPlugingExtractor"]() 
            pluginInstance = pluginExtractor(window)        
            self.plugins.append(pluginInstance)
    
    def getPluginCount(self):
        return len(self.plugins)
    
    def getPluginByIndex(self, index):
        if (index > self.getPluginCount()): raise Exception("The plugin index outs of range") 
        return self.plugins[index]        