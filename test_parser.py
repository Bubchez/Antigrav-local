import unittest
from parser import read_markdown_file

class TestReadMarkdownFile(unittest.TestCase):
    def test_read_existing_markdown_file(self):
        file_path = 'test.md'
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('# Test Markdown File')
        
        content = read_markdown_file(file_path)
        self.assertEqual(content, '# Test Markdown File')
        
        os.remove(file_path)

    def test_read_non_existent_file(self):
        file_path = 'non_existent.md'
        with self.assertRaises(FileNotFoundError):
            read_markdown_file(file_path)

    def test_read_directory(self):
        file_path = 'test_directory'
        os.makedirs(file_path)
        with self.assertRaises(IsADirectoryError):
            read_markdown_file(file_path)
        
        os.rmdir(file_path)

    def test_read_non_markdown_file(self):
        file_path = 'test.txt'
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('This is not a markdown file')
        
        with self.assertRaises(ValueError):
            read_markdown_file(file_path)
        
        os.remove(file_path)

if __name__ == '__main__':
    unittest.main()