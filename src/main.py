from termcolor import colored 
import pyfiglet # New import for ASCII art
import argparse
import sys
from . import api

# --- CLI Command Handlers ---

def handle_random(args):
    """Fetches and prints a random joke with intense formatting."""
    joke = api.fetch_random_joke(args.category)
    
    # Check if the result is an error message
    if joke.startswith("Error:"):
        # Print errors in bold red
        print(colored(joke, 'red', attrs=['bold']))
        sys.exit(1)
    
    # Print header in colored, bold text
    print("\n" + colored("--- CHUCK SAYS: BEWARE! ---", 'yellow', 'on_red', attrs=['bold']))
    # Print joke in a strong visual style
    print(colored(joke, 'white', 'on_red', attrs=['bold']))
    print(colored("--------------------------", 'yellow', 'on_red', attrs=['bold']) + "\n")


def handle_categories(args):
    """Fetches and prints the list of joke categories with color."""
    categories = api.fetch_categories()
    if isinstance(categories, list):
        print(colored("\nAvailable Categories:", 'cyan', attrs=['bold']))
        # Color each category string
        colored_categories = [colored(c, 'green') for c in categories]
        print(" | ".join(colored_categories))
        print("\n")
    else:
        print(colored(categories, 'red'))
        sys.exit(1)


def handle_search(args):
    """Searches for jokes based on a query and highlights the results."""
    jokes = api.search_jokes(args.query)
    if isinstance(jokes, list):
        header_text = f"--- Found {len(jokes)} Joke(s) for '{args.query}' ---"
        print(colored(f"\n{header_text}\n", 'yellow', attrs=['bold']))
        for i, joke in enumerate(jokes, 1):
            # Color the joke text for visual emphasis
            print(f"[{i}] {colored(joke, 'white')}\n")
        print(colored("-" * len(header_text), 'yellow', attrs=['bold']) + "\n")
    else:
        print(colored(jokes, 'red'))
        sys.exit(1)


# --- Main CLI Setup ---

def main():
    """Sets up the argparse CLI and runs the application, displaying an ASCII banner."""
    
    # 1. Print the stylized ASCII art title (The Visual!)
    ascii_banner = pyfiglet.figlet_format("Chuck CLI")
    print(colored(ascii_banner, 'red', attrs=['bold']))
    
    # 2. Setup Argument Parser
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
        help=colored('Optional category to fetch a joke from (e.g., "dev").', 'green')
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
        help=colored('The keyword to search for in jokes.', 'green')
    )
    parser_search.set_defaults(func=handle_search)

    # Parse arguments and call the corresponding handler function
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()