from src.library import Library
from src.book import Book
from src.magazine import Magazine

def main():
    # Створення бібліотеки
    library = Library()

    # Додавання книг
    book1 = Book("1984", "George Orwell", 1949, "978-0451524935")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "978-0446310789")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "978-0743273565")

    library.add_item(book1)
    library.add_item(book2)
    library.add_item(book3)

    # Додавання журналів
    magazine1 = Magazine("National Geographic", "Various", 2023, 1)
    magazine2 = Magazine("Time", "Various", 2023, 15)

    library.add_item(magazine1)
    library.add_item(magazine2)

    # Виведення всіх предметів у бібліотеці
    print("Всі предмети в бібліотеці:")
    for item in library._items:
        print(item)
    print()

    # Пошук за ключовим словом
    keyword = "Orwell"
    print(f"Результати пошуку за ключовим словом '{keyword}':")
    for item in library.search(keyword):
        print(item)
    print()

    # Пошук за роком
    year = 1925
    print(f"Результати пошуку за роком {year}:")
    for item in library.search_by_year(year):
        print(item)
    print()

    # Отримання всіх книг
    print("Всі книги в бібліотеці:")
    for book in library.get_all_books():
        print(book)
    print()

    # Отримання всіх журналів
    print("Всі журнали в бібліотеці:")
    for magazine in library.get_all_magazines():
        print(magazine)
    print()

    # Видалення предмету
    print("Видалення 'To Kill a Mockingbird'")
    library.remove_item(book2)

    # Виведення оновленого списку предметів
    print("Оновлений список предметів у бібліотеці:")
    for item in library._items:
        print(item)
    print()

    # Спроба додати неправильний тип об'єкта
    print("Спроба додати неправильний тип об'єкта:")
    try:
        library.add_item("Це не об'єкт LibraryItem")
    except TypeError as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    main()