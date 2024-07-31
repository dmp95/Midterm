import logging
from decimal import Decimal
from typing import Callable

class Calculation:
   
    def __init__(self, operation: Callable[[Decimal, Decimal], Decimal], a: Decimal, b: Decimal):
 
        self.operation = operation
        self.a = a
        self.b = b
        self.logger = logging.getLogger(__name__)
        self.logger.info("Calculation: %s , operands %s and %s", self.operation.__name__, self.a, self.b)

    def perform_operation(self) -> Decimal:
        try:
            c = self.operation(self.a, self.b)
            self.logger.info("Operation: %s(%s, %s) = %s", self.operation.__name__, self.a, self.b, c)
            return c
        except Exception as e:
            self.logger.error("Operation %s: %s", self.operation.__name__, e)
            raise

    def __repr__(self):
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"