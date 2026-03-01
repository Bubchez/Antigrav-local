
# engine.py

from typing import List
import os

def find_markdown_files(path: str) -> List[str]:
    """
    Scans the given path for markdown files and returns a list of their paths.

    Args:
        path (str): The directory path to scan for markdown files.

    Returns:
        List[str]: A list of paths to markdown files found in the given directory.
    """
    markdown_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files
