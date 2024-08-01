import pytest
from app import App

def test_app_greet_command(capfd, monkeypatch):
    inputs = iter(['Greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    assert e.value.code == 0, "The app did not exit as expected"

    out, err = capfd.readouterr()
    
    assert "Hello, World!" in out, "The 'greet' command did not produce the expected output."
