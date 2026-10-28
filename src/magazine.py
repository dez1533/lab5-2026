from .library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self._issue_number = issue_number

    @property
    def issue_number(self):
        return self._issue_number

    def __str__(self):
        return f"{super().__str__()} - Issue: {self.issue_number}"

    def __repr__(self):
        return f"Magazine('{self.title}', '{self.author}', {self.year}, {self.issue_number})"