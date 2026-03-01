import os
from engine import find_markdown_files
from utils import is_valid_markdown_file

def scan_directory(directory: str) -> list:
    """
    Scans a given directory and returns a list of valid markdown files.

    Args:
        directory (str): The directory to scan for markdown files.

    Returns:
        list: A list of valid markdown file paths.
    """
    markdown_files = find_markdown_files(directory)
    valid_markdown_files = [file for file in markdown_files if is_valid_markdown_file(file)]
    return valid_markdown_files

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python app.py /path/to/directory")
        sys.exit(1)
    directory = sys.argv[1]
    valid_markdown_files = scan_directory(directory)
    for file in valid_markdown_files:
        print(file)