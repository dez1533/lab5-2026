from .library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self._isbn = isbn

    @property
    def isbn(self):
        return self._isbn

    def __str__(self):
        return f"{super().__str__()} - ISBN: {self.isbn}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year}, '{self.isbn}')"