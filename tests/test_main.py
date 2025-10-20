import pytest
from unittest.mock import patch
from io import StringIO
from src import main
import sys


# --- Utility Fixtures ---

@pytest.fixture
def mock_exit(monkeypatch):
    """A fixture to mock sys.exit and track its call."""
    def mock_sys_exit(status):
        raise SystemExit(status)
    monkeypatch.setattr(sys, "exit", mock_sys_exit)
    return mock_sys_exit

# --- Tests for handle_random ---

@patch('sys.stdout', new_callable=StringIO)
@patch('src.api.fetch_random_joke', return_value="A great Chuck Norris joke.")
def test_handle_random_success(mock_api_call, mock_stdout):
    """Tests the random command on successful joke fetch."""
    main.handle_random(main.argparse.Namespace(category=None))
    assert "A great Chuck Norris joke." in mock_stdout.getvalue()
    mock_api_call.assert_called_once()

@patch('sys.stdout', new_callable=StringIO)
@patch('src.api.fetch_random_joke', return_value="Error: API failed.")
def test_handle_random_error(mock_api_call, mock_stdout, mock_exit):
    """Tests the random command when an error is returned from the API function."""
    with pytest.raises(SystemExit) as e:
        main.handle_random(main.argparse.Namespace(category=None))
    assert "Error: API failed." in mock_stdout.getvalue()
    assert e.value.code == 1

# --- Tests for handle_categories ---

@patch('sys.stdout', new_callable=StringIO)
@patch('src.api.fetch_categories', return_value=["dev", "food", "sport"])
def test_handle_categories_success(mock_api_call, mock_stdout):
    """Tests the categories command on successful fetch."""
    main.handle_categories(main.argparse.Namespace())
    output = mock_stdout.getvalue()
    assert "Available Categories" in output
    assert "dev | food | sport" in output
    mock_api_call.assert_called_once()