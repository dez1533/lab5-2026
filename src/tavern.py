"""Клас-менеджер Tavern для управління фентезі-таверною."""

from src.visitor import Visitor
from src.customer import Customer
from src.adventurer import Adventurer
from src.troublemaker import Troublemaker
from src.entities import MenuItem, Event, QuestBoard


class Tavern:
    """Клас-менеджер, що керує відвідувачами, меню, запасами та подіями таверни."""

    def __init__(self, name: str = "П'яний Дракон"):
        self.name = name
        self._visitors = []
        self._menu = []
        self._inventory = {}
        self._events = []
        self.quest_board = QuestBoard()

    def add_visitor(self, visitor: Visitor):
        """Додає відвідувача до таверни з перевіркою типу."""
        if not isinstance(visitor, Visitor):
            raise TypeError("Можна додавати лише об'єкти підкласів Visitor")
        self._visitors.append(visitor)

    def remove_visitor(self, visitor: Visitor):
        """Видаляє відвідувача з таверни."""
        self._visitors.remove(visitor)

    def prepare_item(self, item: MenuItem) -> str:
        """Готує страву або напій з магічними властивостями та додає до меню."""
        if not isinstance(item, MenuItem):
            raise TypeError("Очікується об'єкт MenuItem")
        self._menu.append(item)
        return f"Приготовано: {item.name} (Ефект: {item.magic_effect})"

    def serve_visitor(self, visitor: Visitor, item_name: str = None) -> str:
        """Обслуговує різних типів відвідувачів (поліморфізм + замовлення з меню)."""
        action = visitor.interact()
        if item_name:
            for menu_item in self._menu:
                if menu_item.name.lower() == item_name.lower():
                    visitor.spend_gold(menu_item.price)
                    return f"{action} Подано '{menu_item.name}' ({menu_item.magic_effect})."
        return action

    def organize_event(self, event: Event) -> str:
        """Організовує спеціальну подію в таверні."""
        self._events.append(event)
        return f"У таверні '{self.name}' розпочато подію: {event.title}!"

    def manage_inventory(self, resource: str, quantity: int) -> int:
        """Управління запасами таверни (додавання або списання інгредієнтів)."""
        current = self._inventory.get(resource, 0)
        new_amount = max(0, current + quantity)
        self._inventory[resource] = new_amount
        return new_amount

    def resolve_conflict(self, troublemaker: Troublemaker) -> str:
        """Вирішує конфлікти з проблемними відвідувачами."""
        if not isinstance(troublemaker, Troublemaker):
            return f"{troublemaker.name} поводиться мирно."
        if troublemaker.aggression_level > 8:
            if troublemaker in self._visitors:
                self.remove_visitor(troublemaker)
            return f"Дебошира {troublemaker.name} вигнано з таверни охороною!"
        troublemaker.calm_down()
        return f"Конфлікт залагоджено: {troublemaker.name} заспокоївся."

    def search_visitors(self, keyword: str):
        """Пошук відвідувачів за ім'ям або расою."""
        kw = keyword.lower()
        return [v for v in self._visitors if kw in v.name.lower() or kw in v.race.lower()]

    def filter_by_type(self, visitor_cls):
        """Фільтрація відвідувачів за конкретним підкласом (Customer, Adventurer, Troublemaker)."""
        return [v for v in self._visitors if isinstance(v, visitor_cls)]

    def sort_visitors_by_gold(self, descending: bool = True):
        """Сортування відвідувачів за кількістю золота."""
        return sorted(self._visitors, key=lambda v: v.gold, reverse=descending)

    def __str__(self) -> str:
        return f"Таверна '{self.name}' (Відвідувачів: {len(self._visitors)}, Страв у меню: {len(self._menu)})"

    def __repr__(self) -> str:
        return f"Tavern('{self.name}', visitors={len(self._visitors)})"