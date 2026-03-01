import pytest
from parser import read_markdown_file

def test_read_existing_markdown_file():
    """
    Tests reading an existing markdown file.
    """
    test_file_path = 'test.md'
    with open(test_file_path, 'w', encoding='utf-8') as file:
        file.write('# Test Markdown File')

    assert read_markdown_file(test_file_path) == '# Test Markdown File'

    os.remove(test_file_path)

def test_read_non_existent_file():
    """
    Tests reading a non-existent markdown file.
    """
    with pytest.raises(FileNotFoundError):
        read_markdown_file('non_existent.md')

def test_read_non_markdown_file():
    """
    Tests reading a non-markdown file.
    """
    test_file_path = 'test.txt'
    with open(test_file_path, 'w', encoding='utf-8') as file:
        file.write('This is a test file.')

    with pytest.raises(ValueError):
        read_markdown_file(test_file_path)

    os.remove(test_file_path)