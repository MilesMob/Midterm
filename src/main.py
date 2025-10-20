import argparse
import sys
from . import api

# --- CLI Command Handlers ---

def handle_random(args):
    """Fetches and prints a random joke."""
    joke = api.fetch_random_joke(args.category)
    print("\n--- Chuck Says ---\n")
    print(joke)
    print("\n------------------\n")
    # Gracefully exit if the result is an error message
    if joke.startswith("Error:"):
        sys.exit(1)


def handle_categories(args):
    """Fetches and prints the list of joke categories."""
    categories = api.fetch_categories()
    if isinstance(categories, list):
        print("\nAvailable Categories:\n")
        print(" | ".join(categories))
        print("\n")
    else:
        print(categories)
        sys.exit(1)


def handle_search(args):
    """Searches for jokes based on a query."""
    jokes = api.search_jokes(args.query)
    if isinstance(jokes, list):
        print(f"\n--- Found {len(jokes)} Joke(s) for '{args.query}' ---\n")
        for i, joke in enumerate(jokes, 1):
            print(f"[{i}] {joke}\n")
        print("-------------------------------------------\n")
    else:
        print(jokes)
        sys.exit(1)


# --- Main CLI Setup ---

def main():
    """Sets up the argparse CLI and runs the application."""
    parser = argparse.ArgumentParser(
        description="A command-line tool to fetch and search Chuck Norris Jokes."
    )

    # Setup for subcommands (random, categories, search)
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # 1. 'random' command
    parser_random = subparsers.add_parser('random', help='Get a random Chuck Norris joke.')
    parser_random.add_argument(
        '-c', '--category', 
        type=str, 
        help='Optional category to fetch a joke from (e.g., "dev").'
    )
    parser_random.set_defaults(func=handle_random)

    # 2. 'categories' command
    parser_categories = subparsers.add_parser('categories', help='List all available joke categories.')
    parser_categories.set_defaults(func=handle_categories)

    # 3. 'search' command
    parser_search = subparsers.add_parser('search', help='Search for jokes by keyword.')
    parser_search.add_argument(
        'query', 
        type=str, 
        help='The keyword to search for in jokes.'
    )
    parser_search.set_defaults(func=handle_search)

    # Parse arguments and call the corresponding handler function
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()