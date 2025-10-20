import pytest
from unittest.mock import patch, MagicMock
from src import api
import requests

# --- Mock Data Setup ---

# The test uses the Chuck Norris API, which returns JSON data

@pytest.fixture
def mock_response():
    """A reusable mock response object."""
    return MagicMock()

# --- Tests for fetch_random_joke ---

@patch('requests.get')
def test_fetch_random_joke_success(mock_get, mock_response):
    """Tests successful fetching of a random joke."""
    JOKE_TEXT = "Chuck Norris can divide by zero."
    mock_response.json.return_value = {"value": JOKE_TEXT}
    mock_response.raise_for_status.return_value = None  # Mock a 200 OK status
    mock_get.return_value = mock_response
    
    result = api.fetch_random_joke()
    assert result == JOKE_TEXT
    mock_get.assert_called_with(f"{api.BASE_URL}/random")

@patch('requests.get')
def test_fetch_random_joke_api_error(mock_get):
    """Tests error handling for a bad API status code (e.g., 404)."""
    mock_get.side_effect = requests.exceptions.HTTPError("404 Client Error")
    
    result = api.fetch_random_joke()
    assert result.startswith("Error connecting to API:")

# --- Tests for fetch_categories ---

@patch('requests.get')
def test_fetch_categories_success(mock_get, mock_response):
    """Tests successful fetching of categories."""
    CATEGORIES = ["dev", "food", "sport"]
    mock_response.json.return_value = CATEGORIES
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = api.fetch_categories()
    assert result == CATEGORIES
    mock_get.assert_called_with(f"{api.BASE_URL}/categories")

# --- Tests for search_jokes ---

@patch('requests.get')
def test_search_jokes_success(mock_get, mock_response):
    """Tests successful search with results."""
    SEARCH_QUERY = "test"
    JOKE_1 = "Test joke one."
    JOKE_2 = "Test joke two."
    API_RESPONSE = {
        "total": 2,
        "result": [{"value": JOKE_1}, {"value": JOKE_2}]
    }
    mock_response.json.return_value = API_RESPONSE
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = api.search_jokes(SEARCH_QUERY)
    assert result == [JOKE_1, JOKE_2]
    mock_get.assert_called_with(f"{api.BASE_URL}/search?query={SEARCH_QUERY}")

@patch('requests.get')
def test_search_jokes_no_results(mock_get, mock_response):
    """Tests search when no results are found."""
    SEARCH_QUERY = "nonexistent"
    API_RESPONSE = {"total": 0, "result": []}
    mock_response.json.return_value = API_RESPONSE
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = api.search_jokes(SEARCH_QUERY)
    assert result == f"No jokes found for query: '{SEARCH_QUERY}'"