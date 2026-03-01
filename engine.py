import os

def find_markdown_files(directory: str) -> list:
    """
    Scans a given directory and returns a list of markdown files.

    Args:
        directory (str): The directory to scan for markdown files.

    Returns:
        list: A list of markdown file paths.
    """
    markdown_files = [os.path.join(root, file) for root, _, files in os.walk(directory) for file in files if file.endswith('.md')]
    return markdown_files