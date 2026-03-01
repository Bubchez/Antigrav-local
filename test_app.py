import pytest
from app import scan_directory

def test_scan_directory():
    """
    Tests the scan_directory function with a valid directory.
    """
    test_directory = "test_data"
    expected_files = [
        os.path.join(test_directory, "file1.md"),
        os.path.join(test_directory, "subdir", "file2.md")
    ]
    assert scan_directory(test_directory) == expected_files

def test_scan_directory_no_files():
    """
    Tests the scan_directory function with a directory that contains no markdown files.
    """
    test_directory = "test_data_no_files"
    assert scan_directory(test_directory) == []

def test_scan_directory_invalid_path():
    """
    Tests the scan_directory function with an invalid directory path.
    """
    test_directory = "nonexistent_directory"
    assert scan_directory(test_directory) == []