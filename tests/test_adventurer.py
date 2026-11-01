import unittest
from src.adventurer import Adventurer
from src.entities import MenuItem, Room, Event, QuestBoard


class TestAdventurerAndEntities(unittest.TestCase):
    def setUp(self):
        self.hero = Adventurer("Ґеральт", "Відьмак", 300, "Мисливець на чудовиськ", "S")

    def test_adventurer_attributes(self):
        self.assertEqual(self.hero.name, "Ґеральт")
        self.assertEqual(self.hero.hero_class, "Мисливець на чудовиськ")
        self.assertEqual(self.hero.rank, "S")

    def test_adventurer_interact(self):
        self.assertIn("шукає новий квест", self.hero.interact())

    def test_entities_creation(self):
        item = MenuItem("Зілля магії", 25, "+50 мани")
        room = Room(101, "Люкс", 40)
        event = Event("Турнір бардів", "Музичне змагання")
        board = QuestBoard()
        board.add_quest("Вбити дракона", 500)

        self.assertEqual(item.price, 25)
        self.assertFalse(room.is_occupied)
        self.assertEqual(event.title, "Турнір бардів")
        self.assertEqual(len(board.quests), 1)