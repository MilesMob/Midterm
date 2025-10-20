import argparse
import sys
from .api import fetch_random_joke, fetch_categories, search_jokes, APIError

def handle_random(args):
    """Handler for the 'random' command."""
    joke = fetch_random_joke()
    print(f"Random Joke:\n{joke}")

def handle_categories(args):
    """Handler for the 'categories' command."""
    categories = fetch_categories()
    print("Available Categories:")
    print(", ".join(categories))

def handle_search(args):
    """Handler for the 'search' command."""
    jokes = search_jokes(args.query)
    print(f"Found {len(jokes)} jokes for '{args.query}':")
    for i, joke in enumerate(jokes, 1):
        print(f"  {i}. {joke}")

def main():
    """
    Main entry point for the CLI application.
    Sets up argument parsing and handles command execution.
    """
    parser = argparse.ArgumentParser(
        description="A Chuck Norris Jokes CLI tool."
    )
    subparsers = parser.add_subparsers(
        dest='command', 
        required=True, 
        help='Available commands'
    )

    # Subcommand: random
    parser_random = subparsers.add_parser(
        'random', 
        help='Get a random Chuck Norris joke.'
    )
    parser_random.set_defaults(func=handle_random)

    # Subcommand: categories
    parser_categories = subparsers.add_parser(
        'categories', 
        help='List all available joke categories.'
    )
    parser_categories.set_defaults(func=handle_categories)

    # Subcommand: search
    parser_search = subparsers.add_parser(
        'search', 
        help='Search for jokes by keyword.'
    )
    parser_search.add_argument(
        'query', 
        type=str, 
        help='The keyword to search for.'
    )
    parser_search.set_defaults(func=handle_search)
    
    args = parser.parse_args()

    try:
        # Call the appropriate handler function
        args.func(args)
    except APIError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()