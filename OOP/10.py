class Book:
    def __init__(self, title: str, author: str, pages: int, year: int):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year


class DigitBook(Book):
    def __init__(self, title, author, pages, year, size:int, frm: str):
        super().__init__(title, author, pages, year)
        self.size = size
        self.frm = frm


book1 = Book('Евгений Онегин', 'Пушкин', 666, 1830)
print(book1.__dict__)
book2 = DigitBook('Борис Годунов ', 'Пушкин', 777, 1825, 1024, 'fb2')
print(book2.__dict__)