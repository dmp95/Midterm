from decimal import Decimal
from plugins.plugin_interface import CommandPlugin
from app.functions import Calculator

class DivideCommand(CommandPlugin):
	def __init__(self, plugin_manager):
		self.plugin_manager = plugin_manager

	def execute(self, a,b):
		try:
			result = Calculator.divide(Decimal(a),Decimal(b))
		except ZeroDivisionError:
			return " zero division error"
		return f"{a} / {b} = {result}"

	def get_command_name(self):
		return "Divide"