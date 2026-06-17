# Stworzyc system zarządzania biblioteką
# Book -> title, author, isbn
# dodanie ksiązki, wypozyczenie ksiązki, zwrot ksiązki
# lista dostępnych
# lista wypozyczonych
# dodac klasę Library
#  * dodac User
# -----

def validate_isbn(param_name: str = "isbn"):
    def deco(fn):
        def wrapper(*args, **kwargs):
            pass

        return wrapper

    return deco


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f'Author: {self.author}, Tytuł: {self.title}, ISBN: {self.isbn}'


class Library:
    def __init__(self):
        self.dostepne_ksiazki = []
        self.wypozyczone_ksiazki = []

    def fun_dostepne_ksiazki(self):
        return self.dostepne_ksiazki

    def fun_wypozyczone_ksiazki(self):
        return self.wypozyczone_ksiazki

    def fun_dodaj_ksiazki(self, book: "Book"):
        self.dostepne_ksiazki.append(book)

    def fun_zwroc_ksiazke(self, isbn):
        for book in self.wypozyczone_ksiazki:
            if book.isbn == isbn:
                self.wypozyczone_ksiazki.remove(book)
                self.dostepne_ksiazki.append(book)
                return book
        raise Exception("Ksiązka nie jest z naszej biblioteki")

    @validate_isbn("isbn")
    def fun_wypozycz_ksiazke(self, isbn):
        for book in self.dostepne_ksiazki:
            if book.isbn == isbn:
                self.wypozyczone_ksiazki.append(book)
                self.dostepne_ksiazki.remove(book)
                return book
        raise Exception("Nie ma takiej ksiązki")


biblioteka = Library()
book1 = Book("Pan Tadeusz", 'Adam Mickiewicz', "1234567890")
biblioteka.fun_dodaj_ksiazki(book1)
print(biblioteka.fun_dostepne_ksiazki())
