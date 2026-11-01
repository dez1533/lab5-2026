"""Допоміжні класи таверни: MenuItem, Room, Event, QuestBoard."""


class MenuItem:
    """Страви та напої з магічними властивостями."""

    def __init__(self, name: str, price: int, magic_effect: str):
        self.name = name
        self.price = price
        self.magic_effect = magic_effect

    def __str__(self) -> str:
        return f"{self.name} ({self.price} зол.) [Ефект: {self.magic_effect}]"

    def __repr__(self) -> str:
        return f"MenuItem('{self.name}', {self.price}, '{self.magic_effect}')"


class Room:
    """Приміщення та кімнати для відпочинку в таверні."""

    def __init__(self, number: int, room_type: str, price_per_night: int):
        self.number = number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_occupied = False

    def __str__(self) -> str:
        status = "Зайнята" if self.is_occupied else "Вільна"
        return f"Кімната №{self.number} ({self.room_type}) - {status}"


class Event:
    """Спеціальні події та тематичні вечори в таверні."""

    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description

    def __str__(self) -> str:
        return f"Подія '{self.title}': {self.description}"


class QuestBoard:
    """Дошка оголошень для генерації та управління квестами."""

    def __init__(self):
        self._quests = []

    def add_quest(self, quest_title: str, reward: int):
        self._quests.append({"title": quest_title, "reward": reward})

    @property
    def quests(self):
        return list(self._quests)

    def __str__(self) -> str:
        return f"Дошка квестів (активних завдань: {len(self._quests)})"