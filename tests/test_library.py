import unittest
from src.library import Library
from src.book import Book
from src.magazine import Magazine
from src.library_item import LibraryItem

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("1984", "George Orwell", 1949, "1234567890")
        self.book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "0987654321")
        self.magazine = Magazine("National Geographic", "Various", 2023, 1)

    def test_add_item(self):
        self.library.add_item(self.book1)
        self.assertEqual(len(self.library._items), 1)

    def test_add_invalid_item(self):
        with self.assertRaises(TypeError):
            self.library.add_item("Not a LibraryItem")

    def test_remove_item(self):
        self.library.add_item(self.book1)
        self.library.remove_item(self.book1)
        self.assertEqual(len(self.library._items), 0)

    def test_get_all_books(self):
        self.library.add_item(self.book1)
        self.library.add_item(self.book2)
        self.library.add_item(self.magazine)
        books = self.library.get_all_books()
        self.assertEqual(len(books), 2)
        self.assertIsInstance(books[0], Book)
        self.assertIsInstance(books[1], Book)

    def test_get_all_magazines(self):
        self.library.add_item(self.book1)
        self.library.add_item(self.magazine)
        magazines = self.library.get_all_magazines()
        self.assertEqual(len(magazines), 1)
        self.assertIsInstance(magazines[0], Magazine)

    def test_search(self):
        self.library.add_item(self.book1)
        self.library.add_item(self.book2)
        self.library.add_item(self.magazine)

        results = self.library.search("orwell")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "1984")

    def test_search_by_year(self):
        self.library.add_item(self.book1)
        self.library.add_item(self.book2)
        self.library.add_item(self.magazine)

        results = self.library.search_by_year(1949)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "1984")

    def test_str_representation(self):
        self.library.add_item(self.book1)
        expected = "Library with 1 items"
        self.assertEqual(str(self.library), expected)