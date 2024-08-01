import os
import importlib
import logging
from plugins.plugin_interface import CommandPlugin

class PluginManager:

    def __init__(self, plugin_folders):
 
        self.plugin_folders = plugin_folders
        self.plugins = {}
        self.logger = logging.getLogger(__name__)
        self.load_plugins()

    def load_plugins(self):

        for folder in self.plugin_folders:
            if not os.path.exists(folder):
                self.logger.error("Plugin folder not found: %s", folder)
                continue
            try:
                for filename in os.listdir(folder):
                    if self._is_valid_plugin_file(filename):
                        module_name = filename[:-3]
                        self.logger.info("Loading module: %s", module_name)
                        self._load_module_plugins(module_name, folder)
            except (ImportError, AttributeError, TypeError) as e:
                self.logger.error("Error loading plugins from %s: %s", folder, e)

    def _is_valid_plugin_file(self, filename):
     
        return filename.endswith(".py") and filename != "__init__.py"

    def _load_module_plugins(self, module_name, folder):
 
        try:
            module = importlib.import_module(f"{folder}.{module_name}")
            for attr in dir(module):
                cls = getattr(module, attr)
                if self._is_valid_plugin_class(cls):
                    instance = self._create_plugin_instance(cls)
                    command_name = instance.get_command_name()
                    self.plugins[command_name] = instance
                    self.logger.info("Plugin loaded: %s", command_name)
        except Exception as e:
            self.logger.error("Error loading module %s: %s", module_name, e)

    def _is_valid_plugin_class(self, cls):
       
        return isinstance(cls, type) and issubclass(cls, CommandPlugin) and cls is not CommandPlugin

    def _create_plugin_instance(self, cls):
       
        self.logger.debug("Creating instance of plugin class: %s", cls.__name__)
        return cls(self)

    def get_plugin(self, name):
       
        self.logger.debug("Retrieving plugin with command name: %s", name)
        return self.plugins.get(name)

    def get_all_plugins(self):
   
        self.logger.debug("Retrieving all loaded plugins.")
        return self.plugins
