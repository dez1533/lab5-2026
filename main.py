"""Демонстраційний скрипт роботи симулятора фентезі-таверни (Варіант 8)."""

from src.tavern import Tavern
from src.customer import Customer
from src.adventurer import Adventurer
from src.troublemaker import Troublemaker
from src.entities import MenuItem, Room, Event


def main():
    print("=== СИМУЛЯТОР ФЕНТЕЗІ-ТАВЕРНИ (ВАРІАНТ 8) ===\n")
    tavern = Tavern("П'яний Дракон")

    # 1. Управління запасами та приготування страв
    tavern.manage_inventory("Драконячий перець", 10)
    tavern.manage_inventory("Ельфійський солод", 25)
    drink1 = MenuItem("Ельфійський ель", 15, "+10 до красномовства")
    food1 = MenuItem("Печеня з вогнедишним перцем", 30, "Опір вогню на 1 годину")
    print(tavern.prepare_item(drink1))
    print(tavern.prepare_item(food1))

    # 2. Додавання відвідувачів різних типів
    c1 = Customer("Торін", "Гном", 120, "Ельфійський ель")
    a1 = Adventurer("Ґеральт", "Відьмак", 350, "Мисливець на чудовиськ", "S")
    t1 = Troublemaker("Громмаш", "Орк", 60, 6)
    t2 = Troublemaker("Азог Осквернитель", "Орк", 90, 10)

    for v in (c1, a1, t1, t2):
        tavern.add_visitor(v)

    print(f"\nСтатус: {tavern}")
    print("\n--- Всі відвідувачі у залі (відсортовані за золотом) ---")
    for visitor in tavern.sort_visitors_by_gold():
        print(f"  * {visitor}")

    # 3. Обслуговування відвідувачів (Поліморфізм)
    print("\n--- Обслуговування відвідувачів ---")
    print(tavern.serve_visitor(c1, "Ельфійський ель"))
    print(tavern.serve_visitor(a1, "Печеня з вогнедишним перцем"))

    # 4. Події та дошка квестів
    print("\n--- Організація подій та квестів ---")
    tavern.quest_board.add_quest("Очистити старі катакомби", 200)
    print(tavern.organize_event(Event("Вечір бардівських балад", "Знижки на ель та музика")))
    print(f"{tavern.quest_board}: {tavern.quest_board.quests[0]['title']}")

    # 5. Вирішення конфліктів
    print("\n--- Вирішення конфліктів у таверні ---")
    print(tavern.resolve_conflict(t1))
    print(tavern.resolve_conflict(t2))

    # 6. Пошук
    print("\n--- Пошук відвідувачів за словом 'Гном' ---")
    for res in tavern.search_visitors("Гном"):
        print(f"  Знайдено: {res}")


if __name__ == "__main__":
    main()