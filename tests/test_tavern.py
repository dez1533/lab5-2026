import unittest
from src.tavern import Tavern
from src.customer import Customer
from src.adventurer import Adventurer
from src.troublemaker import Troublemaker
from src.entities import MenuItem, Event


class TestTavern(unittest.TestCase):
    def setUp(self):
        self.tavern = Tavern("Золотий Гоблін")
        self.customer = Customer("Більбо", "Гобіт", 100, "Сидр")
        self.hero = Adventurer("Араґорн", "Людина", 250, "Слідопит", "A")
        self.orc_calm = Troublemaker("Урук", "Орк", 40, 5)
        self.orc_wild = Troublemaker("Азог", "Орк", 80, 10)

        self.tavern.add_visitor(self.customer)
        self.tavern.add_visitor(self.hero)
        self.tavern.add_visitor(self.orc_calm)
        self.tavern.add_visitor(self.orc_wild)

    def test_add_invalid_visitor(self):
        with self.assertRaises(TypeError):
            self.tavern.add_visitor("Не відвідувач")

    def test_prepare_and_serve_visitor(self):
        ale = MenuItem("Магічний сидр", 20, "Нічне бачення")
        self.tavern.prepare_item(ale)
        result = self.tavern.serve_visitor(self.customer, "Магічний сидр")
        self.assertEqual(self.customer.gold, 80)
        self.assertIn("Нічне бачення", result)

    def test_resolve_conflict(self):
        msg1 = self.tavern.resolve_conflict(self.orc_calm)
        self.assertEqual(self.orc_calm.aggression_level, 0)
        self.assertIn("заспокоївся", msg1)

        msg2 = self.tavern.resolve_conflict(self.orc_wild)
        self.assertIn("вигнано", msg2)
        self.assertNotIn(self.orc_wild, self.tavern._visitors)

    def test_inventory_and_events(self):
        amount = self.tavern.manage_inventory("Ельфійський хміль", 15)
        self.assertEqual(amount, 15)
        event_msg = self.tavern.organize_event(Event("Ніч легенд", "Історії біля каміна"))
        self.assertIn("Ніч легенд", event_msg)

    def test_search_filter_and_sort(self):
        orcs = self.tavern.search_visitors("орк")
        self.assertEqual(len(orcs), 2)

        heroes = self.tavern.filter_by_type(Adventurer)
        self.assertEqual(len(heroes), 1)

        sorted_visitors = self.tavern.sort_visitors_by_gold()
        self.assertEqual(sorted_visitors[0].name, "Араґорн")