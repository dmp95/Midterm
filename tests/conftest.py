from decimal import Decimal
import pytest
from faker import Faker
from app import divide
from tests.test_utils import operation_dict
from plugin_file import PluginManager

fake = Faker()

def generate_test_data(num_records):
	for _ in range(num_records):
		a = Decimal(fake.random_number(digits=2))
		b = Decimal(fake.random_number(digits=2)) if _ % 5 != 4 else Decimal(fake.random_number(digit=1))
		operation_func = fake.random_element(elements=list(operation_dict.values()))

		if operation_func is divide:
			b = Decimal('1') if b == Decimal('0') else b

		try:
			if operation_func is divide and b == Decimal('0'):
				expected = "ZeroDivisionError"
			else:
				expected = operation_func(a,b)
		except ZeroDivisionError:
			expected = "ZeroDivisionError"

		yield a,b, operation_func,expected 
		

def pytest_addoption(parser):
	parser.addoption("--num_records",action="store",default=5,type=int, help="test records")

def pytest_generate_tests(metafunc):

    if metafunc.config.getoption("--num_records"):
        if metafunc.definition.get_closest_marker("dynamic_data"):
            if "operand_a" in metafunc.fixturenames and "operand_b" in metafunc.fixturenames and "operation_func" in metafunc.fixturenames and "excepted" in metafunc.fixturenames:
                num_records = int(metafunc.config.getoption("num_records"))
                test_data = list(generate_test_data(num_records))
                metafunc.parametrize("operand_a,operand_b,operation_func,expected", test_data)

@pytest.fixture
def sample_fixture():
    return "sample data"

@pytest.fixture(scope="module")
def loaded_plugins():
  
    plugin_manager = PluginManager(['plugins', 'calculator'])
    plugin_manager.load_plugins()
    plugins = plugin_manager.get_all_plugins()
    
    mock_inputs = {
        'add': (1, 2),
        'subtract': (5, 3),
        'multiply': (2, 3),
        'divide': (6, 2),
        'exponent': (2, 3),
        'greet': (),
        'goodbye': (),
        'help': (),
        'menu': (),
        'exit': ()
    }
    
    return plugins, mock_inputs

def test_sample_fixture(sample_fixture):
    assert sample_fixture == "Sample Data"

