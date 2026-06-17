# Stworzyc system zarządzania biblioteką
# Book -> title, author, isbn
# dodanie ksiązki, wypozyczenie ksiązki, zwrot ksiązki
# lista dostępnych
# lista wypozyczonych
# dodac klasę Library
#  * dodac User
# -----
from datetime import datetime
from functools import wraps


def audit(action: str):
    """
    Dekorator dopisujący wpis do dziennika logó
    :param action:
    :return:
    """

    def deco(fn):
        def wrapper(self: "Library", *args, **kwargs):
            result = fn(self, *args, **kwargs)
            self._audit_log.append(
                f"{datetime.now():%Y-%m-%d %H:%M:%S} | {action} | {args=} {kwargs}"
            )
            return result

        return wrapper

    return deco


def validate_isbn(param_name: str = "isbn"):
    def deco(fn):

        @wraps(fn)
        def wrapper(*args, **kwargs):

            if param_name in kwargs:
                raw = str(kwargs[param_name])
                clean = raw.replace("-", "").strip()
                if len(clean) != 10 or not clean.isdigit():
                    raise ValueError("ISBN musi mieć dokładnie 10 cyfr")
                kwargs[param_name] = clean
                return fn(*args, **kwargs)

            if len(args) < 2:
                raise ValueError("Brak argumentu ISBN")

            raw = str(args[1])
            clean = raw.replace("-", "").strip()
            if len(clean) != 10 or not clean.isdigit():
                raise ValueError("ISBN musi mieć dokładnie 10 cyfr")
            new_args = list(args)
            new_args[1] = clean

            return fn(*tuple(new_args), **kwargs)

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
        self._audit_log = []
        self.dostepne_ksiazki = []
        self.wypozyczone_ksiazki = []

    def fun_dostepne_ksiazki(self):
        return self.dostepne_ksiazki

    def fun_wypozyczone_ksiazki(self):
        return self.wypozyczone_ksiazki

    @audit("dodano")
    def fun_dodaj_ksiazki(self, book: "Book"):
        self.dostepne_ksiazki.append(book)

    @audit("zwrócono")
    def fun_zwroc_ksiazke(self, isbn):
        for book in self.wypozyczone_ksiazki:
            if book.isbn == isbn:
                self.wypozyczone_ksiazki.remove(book)
                self.dostepne_ksiazki.append(book)
                return book
        raise Exception("Ksiązka nie jest z naszej biblioteki")

    @validate_isbn("isbn")
    @audit("wypożyczono")
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
print(biblioteka.fun_wypozycz_ksiazke("1234567890"))
# Author: Adam Mickiewicz, Tytuł: Pan Tadeusz, ISBN: 1234567890
print(biblioteka._audit_log)

while True:
    print("""Menu""")

    try:
        odp = input("Wybierz opcję:")

        if odp == "1":
            pass
        elif odp == "6":
            break
        else:
            print("Błędny wybór")

    except Exception as e:
        print("Bład:", e)
