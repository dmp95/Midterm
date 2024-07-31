from decimal import Decimal
from plugins.plugin_interface import CommandPlugin
from app.functions import Calculator

class AddCommand(CommandPlugin):
	def __init__(self, plugin_manager):
		self.plugin_manager = plugin_manager

	def execute(self, a,b):
		c = Calculator.subtract(Decimal(a),Decimal(b))
		return f"{a} - {b} = {c}"

	def get_command_name(self):
		return "Subtract"