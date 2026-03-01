import os

def find_markdown_files(directory: str) -> list:
    """
    Scans a given directory and returns a list of markdown files.

    Args:
        directory (str): The directory to scan for markdown files.

    Returns:
        list: A list of markdown file paths.
    """
    markdown_files = []
    try:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.md'):
                    markdown_files.append(os.path.join(root, file))
    except PermissionError:
        print(f"Permission denied to access {directory}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return markdown_files