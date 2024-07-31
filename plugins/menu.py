from plugins.plugin_interface import CommandPlugin

class MenuCommand(CommandPlugin):

	def __init__(self,plugin_manager):
		self.plugin_manager = plugin_manager

	def execute(self, *args, **kwargs):
		commands = list(self.plugin_manager.get_all_plugins().keys())
		u_commands = set(commands + [
			"View_History",
			"Clear_History",
			"Delete_History",
			"Save_History"])
		return "Commands: \n " + "\n".join(sorted(u_commands))


	def get_command_name(self):
		return "MENU"