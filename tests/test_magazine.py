import unittest
from src.magazine import Magazine

class TestMagazine(unittest.TestCase):
    def setUp(self):
        self.magazine = Magazine("Test Magazine", "Test Publisher", 2023, 1)

    def test_attributes(self):
        self.assertEqual(self.magazine.title, "Test Magazine")
        self.assertEqual(self.magazine.author, "Test Publisher")
        self.assertEqual(self.magazine.year, 2023)
        self.assertEqual(self.magazine.issue_number, 1)

    def test_str_representation(self):
        expected = "Test Magazine by Test Publisher (2023) - Issue: 1"
        self.assertEqual(str(self.magazine), expected)

    def test_repr_representation(self):
        expected = "Magazine('Test Magazine', 'Test Publisher', 2023, 1)"
        self.assertEqual(repr(self.magazine), expected)