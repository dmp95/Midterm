import logging
from decimal import Decimal

logger = logging.getLogger(__name__)

def add(a: Decimal, b: Decimal) -> Decimal:

    c = a + b
    logger.info("Addition: %s + %s = %s", a, b, c)
    return c

def subtract(a: Decimal, b: Decimal) -> Decimal:
    c = a - b
    logger.info("Subtraction: %s - %s = %s", a, b, c)
    return c

def multiply(a: Decimal, b: Decimal) -> Decimal:
    c = a * b
    logger.info("Multiplication: %s * %s = %s", a, b, c)
    return c

def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        logger.error("Division by zero: %s / %s", a, b)
        raise ZeroDivisionError("exception divide by zero")
    c = a / b
    logger.info("Division: %s / %s = %s", a, b, c)
    return c

def exponent(a: Decimal, b: Decimal) -> Decimal:

    c = a ** b
    logger.info("Exponentiation: %s ** %s = %s", a, b, c)
    return c
