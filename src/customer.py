"""Модуль підкласу Customer (Звичайний відвідувач)."""

from src.visitor import Visitor


class Customer(Visitor):
    """Клас звичайного відвідувача таверни різних рас."""

    def __init__(self, name: str, race: str, gold: int, favorite_drink: str):
        super().__init__(name, race, gold)
        self._favorite_drink = favorite_drink

    @property
    def favorite_drink(self) -> str:
        return self._favorite_drink

    def interact(self) -> str:
        return f"Клієнт {self.name} замовляє свій улюблений напій: {self._favorite_drink}."

    def __str__(self) -> str:
        return f"{super().__str__()} - Улюблений напій: {self._favorite_drink}"

    def __repr__(self) -> str:
        return f"Customer('{self.name}', '{self.race}', {self.gold}, '{self._favorite_drink}')"