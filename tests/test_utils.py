import sys
from io import StringIO
from contextlib import contextmanager
import pytest
from app.functions_defination import add, subtract, multiply, divide, exponent

operation_dict = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide,
    'exponent': exponent
}

def perform_operation_test(a, b, operation_func, expected):
 
    if expected == "ZeroDivisionError":
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            operation_func(a, b)
    else:
        assert operation_func(a, b) == expected

def execute_plugin_tests(plugins, mock_inputs):

    for command_name, plugin in plugins.items():
        if command_name in mock_inputs:
            inputs = mock_inputs[command_name]
            if command_name == "exit":
                with pytest.raises(SystemExit):
                    plugin.execute(*inputs)
            else:
                result = plugin.execute(*inputs)
                assert result is not None, f"{command_name} command returned None"
        else:
            if command_name == "exit":
                with pytest.raises(SystemExit):
                    plugin.execute()
            else:
                result = plugin.execute()
                assert result is not None, f"{command_name} command returned None"

@contextmanager
def suppress_output():

    o_stdout = sys.stdout
    o_stderr = sys.stderr
    sys.stdout = StringIO()
    sys.stderr = StringIO()
    try:
        yield
    finally:
        sys.stdout = o_stdout
        sys.stderr = o_stderr

def suppress_output_decorator(x):
 
    def wrapper(*args, **kwargs):
        with suppress_output():
            return x(*args, **kwargs)
    return wrapper
