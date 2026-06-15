# funkcja - fragment kodu, który mozemy wykonac w dowolnym momencie
from typing import Tuple


# funkcja musi zostac zadeklarowana
# wywołunia funkcji uruchamia kod

# deklaracja funcji
def odejmij():
    print(10 - 4)


odejmij()  # 6


def odejmij(a, b, c):
    print(a - b - c)


# odejmij() # TypeError: odejmij() missing 3 required positional arguments: 'a', 'b', and 'c'
odejmij(4, 5, 6)  # -7


# duck typing
# argumenty o wartościach domyślnych
# symulujemy przeciążanie funkcji liczbą argemntów
def dodaj(a=0, b=0, c=0):
    print(a + b + c)


dodaj()
dodaj(1, 2, )
dodaj(1, 2, 3)
# 0
# 3
# 6

# po nazwie
dodaj(c=9, b=9)  # 18

# mieszane
dodaj(10, 2, c=90)
dodaj(b=90, c=87)  # 177


# dodaj(a=10, 3, 4) # SyntaxError: positional argument follows keyword argument

# print(dodaj(4) + dodaj(5)) # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

# funkcje zwracajace wynik
def mnozenie(a, b):
    return a * b  # zwraca wynik


print(mnozenie(5, 7))  # 35

# przypisac do zmienej
# wypisac co zwrociło
# sprawdzic czy da sie zsumowac wynik dwoch mnozenie()

zmienna = mnozenie(7, 56)
print(f"Wynik mnożenia 7 * 56 = {zmienna}")  # Wynik mnożenia 7 * 56 = 392

print(mnozenie(5, 6) + mnozenie(7, 89))  # 653


# funkcja zwracająca więcej niż jedną wartości
def mnozenie2(a, b):
    return a, b, a * b


print(mnozenie2(5, 6))  # (5, 6, 30)
print(mnozenie2("a", 9))  # ('a', 9, 'aaaaaaaaa')

a, b, wynik = mnozenie2(7, 9)
print(f"{a} * {b} =  {wynik}")  # 7 * 9 =  63


# podpowiedzi typów - nie wymusza typów
def mnozenie3(a: int, b: int) -> Tuple[int, int, int]:
    return a, b, a * b


print(mnozenie3(1, 2))
print(mnozenie3(1, "2"))  # (1, '2', '2')

# narzędzia skanowania kodu
# mypy
# pip install mypy, pyright
# vscode - Pylance
#  cd .\day1\
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonWarsztat-15-06-2026\day1> mypy .\funkcja1.py
# funkcja1.py:16: error: Name "odejmij" already defined on line 9  [no-redef]
# funkcja1.py:21: error: Too many arguments for "odejmij"  [call-arg]
# funkcja1.py:85: error: Argument 2 to "mnozenie3" has incompatible type "str"; expected "int"  [arg-type]
# Found 3 errors in 1 file (checked 1 source file)
