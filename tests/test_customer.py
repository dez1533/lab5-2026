import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Елронд", "Ельф", 150, "Ельфійське вино")

    def test_attributes(self):
        self.assertEqual(self.customer.name, "Елронд")
        self.assertEqual(self.customer.race, "Ельф")
        self.assertEqual(self.customer.gold, 150)
        self.assertEqual(self.customer.favorite_drink, "Ельфійське вино")

    def test_interact(self):
        self.assertEqual(
            self.customer.interact(),
            "Клієнт Елронд замовляє свій улюблений напій: Ельфійське вино."
        )

    def test_str_and_repr(self):
        self.assertIn("Улюблений напій: Ельфійське вино", str(self.customer))
        self.assertEqual(
            repr(self.customer),
            "Customer('Елронд', 'Ельф', 150, 'Ельфійське вино')"
        )