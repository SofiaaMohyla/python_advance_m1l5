# Створення класу "Книга"
class Book:
    def __init__(self, title, isbn, year):
        self.title = title
        self.isbn = isbn
        self.year = year


# Створення класу "Автор"
class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year


# Створення об'єктів "Книга" та "Автор"
books = [
    Book("Тіні забутих предків", "978-966-03-4970-4", 1911),
    Book("Кобзар", "978-966-03-2458-9", 1840),
    Book("Майстер і Маргарита", "978-5-17-104279-6", 1967)
]

authors = [
    Author("Михайло Коцюбинський", 1864),
    Author("Тарас Шевченко", 1814),
    Author("Михайло Булгаков", 1891)
]

# Створення колекції, що містить інформацію про книги та їх авторів
collection = {
    book.isbn: {
        "Назва": book.title,
        "Рік": book.year,
        "Автор": {
            "Ім'я": author.name,
            "Рік народження": author.birth_year
        }
    } for book, author in zip(books, authors)
}

print(collection)
