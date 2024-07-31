import logging
from app.commands import Command


class GreetCommand(Command):

	def __init__ (self, plugin_manager):
		self.plugin_manager = plugin_manager

   	def execute(self. *args, **kwargs):
		return " Calculator App "

	def get_command_name(self):
		return "Greet"
      	  
