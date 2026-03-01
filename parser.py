import os

def read_markdown_file(file_path: str) -> str:
    """
    Reads the content of a markdown file.

    Args:
        file_path (str): The path to the markdown file.

    Returns:
        str: The content of the markdown file.

    Raises:
        FileNotFoundError: If the file does not exist.
        IsADirectoryError: If the path is a directory.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    if os.path.isdir(file_path):
        raise IsADirectoryError(f"{file_path} is a directory, not a file.")
    if not file_path.endswith('.md'):
        raise ValueError(f"The file {file_path} is not a markdown file.")

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content