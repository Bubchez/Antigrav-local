import os
from engine import find_markdown_files

def test_find_markdown_files():
    """
    Tests the find_markdown_files function to ensure it correctly identifies markdown files.
    """
    test_dir = 'test_data'
    os.makedirs(test_dir, exist_ok=True)
    markdown_file = os.path.join(test_dir, 'example.md')
    with open(markdown_file, 'w') as f:
        f.write('# Test Markdown File')

    non_markdown_file = os.path.join(test_dir, 'example.txt')
    with open(non_markdown_file, 'w') as f:
        f.write('This is a test file')

    result = find_markdown_files(test_dir)
    assert markdown_file in result
    assert non_markdown_file not in result

    os.remove(markdown_file)
    os.remove(non_markdown_file)
    os.rmdir(test_dir)