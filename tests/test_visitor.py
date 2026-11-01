import unittest
from src.customer import Customer
from src.visitor import Visitor


class TestVisitor(unittest.TestCase):
    def setUp(self):
        self.visitor = Customer("Торін", "Гном", 100, "Ель")

    def test_attributes_and_encapsulation(self):
        self.assertEqual(self.visitor.name, "Торін")
        self.assertEqual(self.visitor.race, "Гном")
        self.assertEqual(self.visitor.gold, 100)

    def test_spend_gold(self):
        self.visitor.spend_gold(30)
        self.assertEqual(self.visitor.gold, 70)
        with self.assertRaises(ValueError):
            self.visitor.spend_gold(200)

    def test_negative_gold_raises_error(self):
        with self.assertRaises(ValueError):
            Customer("Боржник", "Людина", -10, "Вода")

    def test_cannot_instantiate_abstract_visitor(self):
        with self.assertRaises(TypeError):
            Visitor("Привид", "Нежить", 50)