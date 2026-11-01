"""Модуль базового абстрактного класу Visitor (Відвідувач таверни)."""

from abc import ABC, abstractmethod


class Visitor(ABC):
    """Абстрактний базовий клас для всіх відвідувачів фентезі-таверни."""

    def __init__(self, name: str, race: str, gold: int):
        if gold < 0:
            raise ValueError("Кількість золота не може бути від'ємною")
        self._name = name
        self._race = race
        self._gold = gold

    @property
    def name(self) -> str:
        return self._name

    @property
    def race(self) -> str:
        return self._race

    @property
    def gold(self) -> int:
        return self._gold

    def spend_gold(self, amount: int):
        """Витрачає золото відвідувача."""
        if amount > self._gold:
            raise ValueError("Недостатньо золота")
        self._gold -= amount

    @abstractmethod
    def interact(self) -> str:
        """Поліморфний метод взаємодії відвідувача в таверні."""
        pass

    def __str__(self) -> str:
        return f"{self._name} ({self._race}) - Золото: {self._gold}"

    def __repr__(self) -> str:
        return f"Visitor('{self._name}', '{self._race}', {self._gold})"