# Chuck Norris Jokes CLI
[![Tests](https://github.com/MilesMob/Midterm/actions/workflows/tests.yml/badge.svg)](https://github.com/MilesMob/Midterm/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Project Description

A robust, AI-assisted command-line interface (CLI) built with Python and `argparse` to fetch and display jokes from the Chuck Norris Jokes API. This project demonstrates best practices in Python development, including API integration, comprehensive testing with mocking, and automated Continuous Integration (CI) using GitHub Actions.

## Features

* **Random Jokes:** Quickly fetch a single, random Chuck Norris joke.
* **Categories:** List all available joke categories to refine search.
* **Keyword Search:** Search for jokes containing a specific query string.
* **Professional Standards:** Fully tested with `pytest` and mocked API calls.
* **Error Handling:** Gracefully handles network issues and API errors.

## Installation and Setup

This project requires Python 3.10 or later.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git)
    cd chuck_cli
    ```

2.  **Create a virtual environment (Recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The CLI is executable via `python -m src.main`. Use the `--help` flag for a list of commands.

### 1. Get a Random Joke

```bash
python -m src.main random