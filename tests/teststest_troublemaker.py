import unittest
from src.troublemaker import Troublemaker


class TestTroublemaker(unittest.TestCase):
    def setUp(self):
        self.trouble = Troublemaker("Громмаш", "Орк", 50, 7)

    def test_attributes_and_calm_down(self):
        self.assertEqual(self.trouble.aggression_level, 7)
        self.trouble.calm_down()
        self.assertEqual(self.trouble.aggression_level, 0)

    def test_interact(self):
        self.assertIn("влаштовує бійку", self.trouble.interact())