from unittest.mock import patch
import pytest
from main import calculate_and_print, main, App

def test_calculate_and_print_addition(capsys):

    calculate_and_print("5", "6", "add")
    captured = capsys.readouterr()
    assert "5 add 6 = 11" in captured.out

def test_calculate_and_print_invalid_number(capsys):
 
    calculate_and_print("one", "2", "add")
    captured = capsys.readouterr()
    assert "one or 2 is not a valid number." in captured.out

def test_calculate_and_print_unknown_operation(capsys):

    calculate_and_print("1", "2", "unknown")
    captured = capsys.readouterr()
    assert "Unknown Operation" in captured.out

def test_calculate_and_print_divide_by_zero(capsys):

    calculate_and_print("1", "0", "divide")
    captured = capsys.readouterr()
    expected_output = "Cannot divide by zero."
    assert expected_output in captured.out, f"Expected '{expected_output}' in output but got {captured.out}"

@patch('builtins.input', side_effect=["exit"])
@patch('main.CommandHandler')
@patch('main.PluginManager')
@patch('main.load_dotenv')
def test_app_start(mock_load_dotenv, mock_plugin_manager, mock_command_handler, mock_input):

    app = App()
    with pytest.raises(SystemExit):
        app.start()
    mock_input.assert_called_once_with(">>> ")
    mock_command_handler().execute_command.assert_any_call('menu')

@patch('sys.argv', ['main.py'])
@patch('builtins.input', side_effect=["exit"])
@patch('main.CommandHandler')
@patch('main.PluginManager')
@patch('main.load_dotenv')
def test_main_no_arguments(mock_load_dotenv, mock_plugin_manager, mock_command_handler, mock_input):

    with pytest.raises(SystemExit):
        main()
    mock_input.assert_called_once_with(">>> ")

@patch('sys.argv', ['main.py', '1', '2', 'add'])
@patch('main.calculate_and_print')
def test_main_with_arguments(mock_calculate_and_print):
   
    main()
    mock_calculate_and_print.assert_called_once_with('1', '2', 'add')

@patch('sys.argv', ['main.py', '1', '2'])
@patch('sys.exit')
def test_main_invalid_arguments(mock_sys_exit):

    main()
    mock_sys_exit.assert_called_once_with(1)

@patch('builtins.input', side_effect=["greet", "exit"])
@patch('main.CommandHandler')
@patch('main.PluginManager')
@patch('main.load_dotenv')
def test_app_handle_commands(mock_load_dotenv, mock_plugin_manager, mock_command_handler, mock_input):

    mock_command_handler_instance = mock_command_handler.return_value
    mock_command_handler_instance.execute_command.return_value = "Hello!"
   
    app = App()
    with pytest.raises(SystemExit):
        app.start()
   
    assert mock_input.call_count == 2
    mock_command_handler_instance.execute_command.assert_any_call("Greet")
    assert "Hello!" in mock_command_handler_instance.execute_command.return_value
