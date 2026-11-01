"""Модуль підкласу Adventurer (Шукач пригод / Герой)."""

from src.visitor import Visitor


class Adventurer(Visitor):
    """Клас героя з особливими потребами, рангом та історіями."""

    def __init__(self, name: str, race: str, gold: int, hero_class: str, rank: str):
        super().__init__(name, race, gold)
        self._hero_class = hero_class
        self._rank = rank

    @property
    def hero_class(self) -> str:
        return self._hero_class

    @property
    def rank(self) -> str:
        return self._rank

    def interact(self) -> str:
        return f"Герой {self.name} ({self._hero_class}, ранг {self._rank}) шукає новий квест на дошці."

    def __str__(self) -> str:
        return f"{super().__str__()} - Клас: {self._hero_class} (Ранг: {self._rank})"

    def __repr__(self) -> str:
        return f"Adventurer('{self.name}', '{self.race}', {self.gold}, '{self._hero_class}', '{self._rank}')"