import os
import pytest
from engine import find_markdown_files
from utils import is_valid_markdown_file

class TestReadMarkdownFile:
    def test_read_directory(self):
        # Test reading a directory with markdown files
        directory = 'test_data/markdowns'
        markdown_files = find_markdown_files(directory)
        assert len(markdown_files) == 2  # Assuming there are 2 markdown files in the directory

    def test_read_existing_markdown_file(self):
        # Test reading an existing markdown file
        file_path = 'test_data/markdowns/example.md'
        assert is_valid_markdown_file(file_path)

    def test_read_non_existent_file(self):
        # Test reading a non-existent file
        file_path = 'test_data/markdowns/non_existent.md'
        assert not is_valid_markdown_file(file_path)

    def test_read_non_markdown_file(self):
        # Test reading a non-markdown file
        file_path = 'test_data/non_markdowns/example.txt'
        assert not is_valid_markdown_file(file_path)
```

This code snippet includes the necessary imports and defines a test class `TestReadMarkdownFile` with four test methods to verify the functionality of the `find_markdown_files` and `is_valid_markdown_file` functions.