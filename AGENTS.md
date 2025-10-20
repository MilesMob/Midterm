# Project Name: Chuck Norris Jokes CLI

## Overview
A Python command-line interface (CLI) tool for interacting with the public Chuck Norris Jokes API. The tool must be built using `argparse` and demonstrate professional testing practices (mocking) and CI/CD setup.

## API Integration
- **API:** Chuck Norris Jokes API
- **Base URL:** `https://api.chucknorris.io/`
- **Key Endpoints:**
    - `/jokes/random`: Returns a random joke (JSON object with a 'value' key).
    - `/jokes/categories`: Returns a JSON array of strings (categories).
    - `/jokes/search?query={text}`: Returns a JSON object with a 'result' array of jokes.
- **Constraint:** Must handle API errors (e.g., connection issues, invalid search queries) gracefully.

## CLI Commands
The main entry point is `python -m src.main [command] [options]`.
1.  `chuck random`: Gets a single, random Chuck Norris joke.
2.  `chuck categories`: Lists all available joke categories.
3.  `chuck search <query>`: Searches for jokes containing the provided `<query>`. The output should list the joke text.

## Technical Stack
- **Language:** Python 3.10+
- **CLI:** `argparse` (using subparsers for commands)
- **API Client:** `requests`
- **Testing:** `pytest` with `unittest.mock` for mocking API calls.
- **CI/CD:** GitHub Actions.

## Code Organization
- `src/api.py`: Contains all functions responsible for making HTTP requests (e.g., `fetch_random_joke`, `fetch_categories`, `search_jokes`). All real API calls must be isolated here for easy mocking.
- `src/main.py`: Contains `argparse` setup, argument parsing logic, and the main entry point (`if __name__ == "__main__":`).
- `tests/test_api.py`: Tests for API interaction functions using mocks.
- `tests/test_main.py`: Tests for CLI command execution logic.

## Standards
- All functions must have clear docstrings.
- Adhere to PEP 8 style guidelines.
- **Crucial:** All tests must use mocking to prevent real network requests.