"""Модуль підкласу Troublemaker (Проблемний відвідувач)."""

from src.visitor import Visitor


class Troublemaker(Visitor):
    """Проблемний відвідувач, що створює конфлікти в таверні."""

    def __init__(self, name: str, race: str, gold: int, aggression_level: int):
        super().__init__(name, race, gold)
        self._aggression_level = aggression_level

    @property
    def aggression_level(self) -> int:
        return self._aggression_level

    def calm_down(self):
        """Знижує рівень агресії до нуля після вирішення конфлікту."""
        self._aggression_level = 0

    def interact(self) -> str:
        return f"Дебошир {self.name} влаштовує бійку! Рівень агресії: {self._aggression_level}."

    def __str__(self) -> str:
        return f"{super().__str__()} - Рівень агресії: {self._aggression_level}"

    def __repr__(self) -> str:
        return f"Troublemaker('{self.name}', '{self.race}', {self.gold}, {self._aggression_level})"