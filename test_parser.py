import os
import pytest
from engine import find_markdown_files
from utils import is_valid_markdown_file

def test_find_markdown_files():
    """
    Tests the find_markdown_files function.
    """
    test_dir = 'test_data'
    os.makedirs(test_dir, exist_ok=True)
    try:
        with open(os.path.join(test_dir, 'test.md'), 'w') as f:
            f.write('# Test Markdown')
        with open(os.path.join(test_dir, 'test.txt'), 'w') as f:
            f.write('Test Text')

        markdown_files = find_markdown_files(test_dir)
        assert len(markdown_files) == 1
        assert markdown_files[0].endswith('test.md')
    finally:
        os.remove(os.path.join(test_dir, 'test.md'))
        os.remove(os.path.join(test_dir, 'test.txt'))
        os.rmdir(test_dir)


def test_is_valid_markdown_file():
    """
    Tests the is_valid_markdown_file function.
    """
    test_file = 'test.md'
    with open(test_file, 'w') as f:
        f.write('# Test Markdown')

    assert is_valid_markdown_file(test_file)
    os.remove(test_file)