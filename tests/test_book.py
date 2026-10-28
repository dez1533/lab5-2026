import unittest
from src.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("Test Book", "Test Author", 2023, "1234567890")

    def test_attributes(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.year, 2023)
        self.assertEqual(self.book.isbn, "1234567890")

    def test_str_representation(self):
        expected = "Test Book by Test Author (2023) - ISBN: 1234567890"
        self.assertEqual(str(self.book), expected)

    def test_repr_representation(self):
        expected = "Book('Test Book', 'Test Author', 2023, '1234567890')"
        self.assertEqual(repr(self.book), expected)