#!/usr/bin/env python3
import sys
import requests
import time


def fetch_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"URL: {url}")
        print(response.text)
        print("=" * 20)
    else:
        print(f"Failed to fetch URL: {
              url} (Status code: {response.status_code})")


def fetch_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.read().strip().split('\n')
    return urls


def print_help():
    help_text = """
Usage:
    ./script.py <url>         : Fetch content from a single URL
    ./script.py -f <file>     : Fetch content from URLs listed in a file (one URL per line)
    ./script.py --file <file> : Same as -f, fetch content from URLs listed in a file
    ./script.py -h, --help    : Show this help message
    """
    print(help_text)


if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] in ['-h', '--help']:
        print_help()
        sys.exit(0)

    if len(sys.argv) == 2:
        # Single URL provided as command-line argument
        url_or_file = sys.argv[1]
        if url_or_file.startswith('-'):
            print("Invalid argument. Use -h or --help for usage instructions.")
            sys.exit(1)
        if url_or_file.endswith('.txt'):
            urls = fetch_urls_from_file(url_or_file)
        else:
            urls = [url_or_file]
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--file'):
        # File path provided to fetch URLs from
        file_path = sys.argv[2]
        urls = fetch_urls_from_file(file_path)
    else:
        print("Invalid arguments. Use -h or --help for usage instructions.")
        sys.exit(1)

    for url in urls:
        fetch_url(url)
        # Pause for 15 seconds between requests to handle rate limiting
        time.sleep(15)
