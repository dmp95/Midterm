import logging
from decimal import Decimal, InvalidOperation
from plugins.plugin_interface import CommandPlugin
from app.calculations import Calculations

class CommandHandler:
    def __init__(self, plugin_manager):
        self.plugin_manager = plugin_manager
        self.logger = logging.getLogger(__name__)

    def execute_command(self, name, *args):
        self.logger.info("Executing command: %s", name)

        history_commands = {
            "view_history": lambda: Calculations.view_history().to_string(),
            "clear_history": lambda: "Calculation history cleared." if not Calculations.clear_history() else "Failed to clear history.",
            "delete_history": lambda: "Calculation history deleted." if not Calculations.delete_history() else "Failed to delete history.",
        }

        if name in history_commands:
            self.logger.info("Handling history command: %s", name)
            return history_commands[name]()
        
        command = self.plugin_manager.get_plugin(name)
        if command:
            self.logger.info("Found command plugin: %s", name)
            try:
                if name in ['add', 'subtract', 'multiply', 'divide', 'exponent']:
                    if len(args) < 2:
                        operand_a = Decimal(input("Enter first operand: "))
                        operand_b = Decimal(input("Enter second operand: "))
                        self.logger.info("Operands: %s, %s", operand_a, operand_b)
                        return command.execute(operand_a, operand_b)
                    return command.execute(*args)
                return command.execute(*args)
            except InvalidOperation:
                self.logger.error("Invalid number input.")
                return "Invalid number input."
            except ZeroDivisionError:
                self.logger.error("Cannot divide by zero.")
                return "Cannot divide by zero."
            except Exception as e:
                self.logger.error("Error executing command %s: %s", name, e)
                return f"Error executing command {name}: {e}"
        
        self.logger.warning("Command not found: %s", name)
        return "Command not found."

    def get_command(self, name):
        self.logger.debug("Retrieving command: %s", name)
        return self.plugin_manager.get_plugin(name)
