import requests

BASE_URL = "https://api.chucknorris.io"

class APIError(Exception):
    """Custom exception for API-related errors."""
    pass

def _fetch(endpoint, params=None):
    """
    Internal helper function to handle API calls and common errors.
    """
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.HTTPError as e:
        # Specific handling for errors like search with no results
        if response.status_code == 404:
            raise APIError("Resource not found or invalid request.")
        raise APIError(f"HTTP error occurred: {e}. Status code: {response.status_code}")
    except requests.exceptions.ConnectionError:
        raise APIError("Connection error: Could not reach the API.")
    except requests.exceptions.Timeout:
        raise APIError("The request timed out.")
    except requests.exceptions.RequestException as e:
        raise APIError(f"An unexpected request error occurred: {e}")

def fetch_random_joke():
    """
    Fetches a single random Chuck Norris joke.

    :return: The joke string.
    :raises APIError: If the API call fails.
    """
    data = _fetch("/jokes/random")
    return data.get('value')

def fetch_categories():
    """
    Fetches a list of all available joke categories.

    :return: A list of strings (categories).
    :raises APIError: If the API call fails.
    """
    data = _fetch("/jokes/categories")
    return data

def search_jokes(query):
    """
    Searches for jokes containing the given query string.

    :param query: The search term.
    :return: A list of joke strings.
    :raises APIError: If the API call fails or no results are found.
    """
    if not query:
        raise APIError("Search query cannot be empty.")
    
    data = _fetch("/jokes/search", params={'query': query})
    
    # The search endpoint returns a 'result' list, which might be empty
    jokes = [item['value'] for item in data.get('result', [])]
    
    if not jokes:
        raise APIError(f"No jokes found for query: '{query}'")
        
    return jokes