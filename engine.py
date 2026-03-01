import os

def find_markdown_files(directory: str) -> list:
    """
    Scans a given directory and returns a list of markdown files.

    Args:
        directory (str): The directory to scan for markdown files.

    Returns:
        list: A list of markdown file paths.
    """
    return [os.path.join(root, file) for root, _, files in os.walk(directory) if file.endswith('.md')]


def is_valid_markdown_file(file_path: str) -> bool:
    """
    Validates if the given file path is a valid markdown file.

    Args:
        file_path (str): The file path to validate.

    Returns:
        bool: True if the file path is a valid markdown file, False otherwise.
    """
    return os.path.isfile(file_path) and file_path.endswith('.md')