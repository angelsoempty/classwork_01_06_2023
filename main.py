class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        print("Назва книги: ", self.title)
        print("Автор: ", self.author)
book1 = Book("Багатий тато Бідний тато", "Роберт Кіосакі")
book1.get_info()
