import unittest
from src.library_item import LibraryItem

class TestLibraryItem(unittest.TestCase):
    def setUp(self):
        self.item = LibraryItem("Test Title", "Test Author", 2023)

    def test_attributes(self):
        self.assertEqual(self.item.title, "Test Title")
        self.assertEqual(self.item.author, "Test Author")
        self.assertEqual(self.item.year, 2023)

    def test_str_representation(self):
        expected = "Test Title by Test Author (2023)"
        self.assertEqual(str(self.item), expected)

    def test_repr_representation(self):
        expected = "LibraryItem('Test Title', 'Test Author', 2023)"
        self.assertEqual(repr(self.item), expected)