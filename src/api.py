import requests
import json
import sys

# Base URL for the Chuck Norris Jokes API
BASE_URL = "https://api.chucknorris.io/jokes"

def fetch_random_joke(category=None):
    """
    Fetches a random joke from the Chuck Norris API.

    Args:
        category (str, optional): The category to fetch the joke from. Defaults to None.

    Returns:
        str: The joke text, or an error message if the request fails.
    """
    endpoint = f"{BASE_URL}/random"
    if category:
        endpoint += f"?category={category}"

    try:
        response = requests.get(endpoint)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        data = response.json()
        return data.get('value', 'Error: Joke not found.')
    except requests.exceptions.RequestException as e:
        return f"Error connecting to API: {e}"
    except json.JSONDecodeError:
        return "Error: Could not parse API response."


def fetch_categories():
    """
    Fetches the list of all available joke categories.

    Returns:
        list or str: A list of category strings, or an error message.
    """
    endpoint = f"{BASE_URL}/categories"
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()  # This returns a list of strings
    except requests.exceptions.RequestException as e:
        return f"Error connecting to API: {e}"
    except json.JSONDecodeError:
        return "Error: Could not parse API response."


def search_jokes(query):
    """
    Searches for jokes containing the specified query string.

    Args:
        query (str): The search term.

    Returns:
        list or str: A list of joke strings, or an error message.
    """
    endpoint = f"{BASE_URL}/search?query={query}"
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        data = response.json()
        
        # The API returns a list of joke objects under the 'result' key
        jokes = [item.get('value') for item in data.get('result', [])]
        
        if not jokes:
            return f"No jokes found for query: '{query}'"
            
        return jokes
    except requests.exceptions.RequestException as e:
        return f"Error connecting to API: {e}"
    except json.JSONDecodeError:
        return "Error: Could not parse API response."