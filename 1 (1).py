class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):

        print("제목:", self.title)
        print("저자:", self.author)
        print("가격:", self.price)

    def __eq__(self, other):

        if isinstance(other, Book):
            return self.price == other.price
        return False


book1 = Book("파이썬 프로그래밍", "금", 30000)
book2 = Book("자바 프로그래밍", "은", 30000)


book1.display_info()
book2.display_info()

print("책1과 책2의 가격이 같나요?", book1 == book2)