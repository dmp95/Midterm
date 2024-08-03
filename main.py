import os
import sys
import logging
from decimal import Decimal, InvalidOperation
from dotenv import load_dotenv
from plugin_file import PluginManager
from command_handler import CommandHandler
from logging_config import setup_logging

# Configure the environment and logging
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
load_dotenv()
setup_logging()

logger = logging.getLogger(__name__)

def calculate_and_print(a_string: str, b_string: str, operation_string: str) -> None:
    """
    Perform a calculation using the specified operation and print the result.

    Args:
        a_string (str): The first number as a string.
        b_string (str): The second number as a string.
        operation_string (str): The operation to perform.
    """
    logger.info(f"Calculating: {a_string} {operation_string} {b_string}")

    try:
        a = Decimal(a_string)
        b = Decimal(b_string)
    except InvalidOperation:
        error_message = f"{a_string} or {b_string}"
        logger.error(error_message)
        print(error_message)
        return

    try:
        plugin_manager = PluginManager(['plugins', 'calculator'])
        plugin_manager.load_plugins()

        operation_plugin = plugin_manager.get_plugin(operation_string)
        if not operation_plugin:
            error_message = f"Unknown Operation"
            logger.warning(error_message)
            print(error_message)
            return
        
        result = operation_plugin.execute(a, b)
        success_message = f"{a_string} {operation_string} {b_string} = {result}"
        logger.info(success_message)
        print(success_message)
    except ZeroDivisionError:
        error_message = "Cannot divide by zero"
        logger.error(error_message)
        print(f"An error occurred: {error_message}")
    except Exception as e:
        logger.exception("Error performing calculation")
        print(f"Error performing calculation: {e}")

class App:
    def __init__(self):
        """
        Initialize the application with a plugin manager and command handler.
        """
        self.plugin_manager = PluginManager(['plugins', 'calculator'])
        self.command_handler = CommandHandler(self.plugin_manager)
        self.running = True

        # Set up logging configuration
        log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
        logging.basicConfig(level=log_level)
        self.logger = logging.getLogger(__name__)

        if os.getenv('API_KEY'):
            self.logger.info("API Key Loaded")

    def start(self) -> None:
        """
        Start the application and handle user commands.
        """
        self.logger.info("Starting the application")
        print(self.command_handler.execute_command('menu'))
        print("Type 'exit' to exit.")

        while self.running:
            try:
                user_input = input(">>> ").strip()
                if user_input.lower() == "exit":
                    self.running = False
                    print("Exiting the application.")
                    self.logger.info("Exiting the application")
                    raise SystemExit(0)

                self.logger.info(f"Executing command: {user_input}")
                response = self.command_handler.execute_command(user_input)
                if response:
                    print(response)

            except ZeroDivisionError:
                error_message = "Cannot divide by zero"
                self.logger.error(error_message)
                print(f"An error occurred: {error_message}")
            except Exception as e:
                self.logger.exception("An error occurred")
                print(f"An error occurred: {e}")

def main() -> None:
    """
    Main function to handle command line arguments and application startup.
    """
    if len(sys.argv) == 1:
        print("No arguments provided. Entering command mode.")
        print("Usage: python main.py <number1> <number2> <operation>")
        print("Or run without arguments to enter command mode.")
        app = App()
        app.start()
    elif len(sys.argv) == 4:
        _, a, b, operation = sys.argv
        calculate_and_print(a, b, operation)
    else:
        print("Usage: python main.py <number1> <number2> <operation>")
        print("Or run without arguments to enter command mode.")
        sys.exit(1)

if __name__ == '__main__':
    main()
