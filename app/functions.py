import logging
from decimal import Decimal
from typing import Callable
from .calculation import Calculation
from .history import Calculations
from .functions_defination import add, subtract, multiply, divide, exponent

class Calculator:
   
    logger = logging.getLogger(__name__)

    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
       
        try:
            Calculator.logger.info("Operation: %s(%s, %s)", operation.__name__, a, b)
            calculation = Calculation(operation, a, b)
            result = calculation.perform_operation()
            Calculations.add_calculation(calculation)
            Calculator.logger.info("Result: %s", result)
            return result
        except ZeroDivisionError as e:
            Calculator.logger.error("Error: %s", e)
            raise e
        except Exception as e:
            Calculator.logger.error("Error: %s", e)
            return Decimal('0')

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, divide)

    @staticmethod
    def exponent(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, exponent)