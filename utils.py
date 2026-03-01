
import os

def is_valid_markdown_file(file_path: str) -> bool:
    """
    Validates if the given file path is a valid markdown file.

    Args:
        file_path (str): The file path to validate.

    Returns:
        bool: True if the file path is a valid markdown file, False otherwise.
    """
    if not os.path.exists(file_path):
        return False
    if not os.path.isfile(file_path):
        return False
    if not file_path.endswith('.md'):
        return False
    return True
