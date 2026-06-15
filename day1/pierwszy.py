# https://peps.python.org/pep-0008/ - formtowanie kodu
# snake_case
# ctrl alt l - pomaga w formatowaniu kodu
import sys

print("")
print('')

# blake

print("pierwsza linia")
print('pierwsza linia')

# ctrl d - powielanie

# ctrl / - komentarz
# print('pierwszy")
#   File "C:\Users\CSComarch\PycharmProjects\PythonWarsztat-15-06-2026\day1\pierwszy.py", line 15
#     print('pierwszy")
#           ^
# SyntaxError: unterminated string literal (detected at line 15)
#
# Process finished with exit code

"""
komentarz
    wielolinijkowy (dokumentacja)"""

info = """
tekst
wielolinijkowy
    zachowuje
        formatowanie"""

print(info)
# "tekst
# wielolinijkowy
#     zachowuje
#         formatowanie"

# typowanie dynamiczne
print(type(info))  # <class 'str'>
info = 90
print(type(info))  # <class 'int'> liczba całkowita

print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300, str_digits_check_threshold=640)

info = "Radek"
print(info)  # Radek

print("12" + "45")  # konkatenacja ->  1245
print(12 * "40")  # 404040404040404040404040

# print("12" + 40) # TypeError: can only concatenate str (not "int") to str
# silne typowanie - nie zmienia samodzielnie typów


# float - zmiennoprzecinkowe
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
# min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

# błąd zaokrąglenia
print(0.1 + 0.9)  # 1.0
print(0.1 + 0.2)  # 0.30000000000000004

#  For example, in a floating-point arithmetic with five base-ten digits,
#  the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# decimla() - pozwal ominąc problem błedu zaoktrąglenia

# boolean
# typ logiczny
# True, False
# 1, 0

print(bool(100))  # True
print(bool("radek"))  # True

print(bool(""))  # False
print(bool(0))  # False

print(bool("0"))

# rzutowanie
print(int("0"))  # 0

# kolekcje
# przechowuje dowolną ilośc danych i dowolny typ na raz

# lista - zachowuje kolejność przy dodwaniu elementów, mutowalna
imiona = ["Jan", "Piotr", "Anna", "Nadia", "Michał"]
print(imiona)  # ['Jan', 'Piotr', 'Anna', 'Nadia', 'Michał']
print(type(imiona))  # <class 'list'>

# ['Jan', 'Piotr', 'Anna', 'Nadia', 'Michał']
#    0       1        2        3        4
#    -5      -4       -3       -2       -1
print(imiona[1])  # Piotr
print(imiona[-1])  # Michał
print(imiona[len(imiona) - 1])  # Michał
print(imiona[-1])  # Michał ostatni element

print(imiona[-2])

# sliceowanie - fragment listy
print(imiona[2:4])  # ['Anna', 'Nadia']
print(imiona[1:])  # ['Piotr', 'Anna', 'Nadia', 'Michał']

print(imiona[2:7])  # ['Anna', 'Nadia', 'Michał']
print(imiona[10:34])  # []

print(imiona[-2:0])  # [] [3:0]
print(imiona[0:-2])  # [0:3] # ['Jan', 'Piotr', 'Anna']

imiona_p = imiona[::2]  # [start:stop:krok]
print(imiona_p)  # ['Jan', 'Anna', 'Michał']

lista_p = list()
lista_p2 = []
print(lista_p)  # []
print(lista_p2)  # []

lista_p.append("Karol")
lista_p.append("Radek")
lista_p.append("Tomek")
lista_p.append("Anna")
print(lista_p)  # ['Karol', 'Radek', 'Tomek', 'Anna']

lista_p.insert(1, "Jan")  # na wskazanym indeksie
print(lista_p)  # ['Karol', 'Jan', 'Radek', 'Tomek', 'Anna']

lista_p.append("Jan")
print(lista_p)  # ['Karol', 'Jan', 'Radek', 'Tomek', 'Anna', 'Jan']

lista_p.remove("Jan")  # usunie pierwszy napotkany
print(lista_p)
# ['Karol', 'Radek', 'Tomek', 'Anna', 'Jan']

# garbage collector

del imiona[3]
print(imiona)

del lista_p2  # usunięcie zmiennej
# print(lista_p2) # NameError: name 'lista_p2' is not defined. Did you mean: 'lista_p'?

# numerowanie kolekcji
# enumerate()
imen = enumerate(imiona, start=111)
# for i in imen:
#     print(i)
# (114, 'Michał')
# 114, 'Michal'
# for i in imen:
#     print(i[0], i[1])
# 111 Jan
# 112 Piotr
# 113 Anna
# 114 Michał

a, b = (114, 'Michał')
print(a, b)  # 114 Michał

for index, wartosc in imen:
    print(f"index -> {index}, wartosc -> {wartosc}")
# index -> 111, wartosc -> Jan
# index -> 112, wartosc -> Piotr
# index -> 113, wartosc -> Anna
# index -> 114, wartosc -> Michał

print("index -> {}, wartosc -> {}".format(index, wartosc))  # index -> 114, wartosc -> Michał

print("index:", index, "wartość:", wartosc)  # index: 114 wartość: Michał

# sep
# string inserted between values, default a space.
# end
# string appended after the last value, default a newline.
print("index:", index, "wartość:", wartosc, sep="----")  # index:----114----wartość:----Michał

# lazy
# dedykowany do logów
print("a: %i b: %s" % (index, wartosc))  # a: 114 b: Michał
# print("a: %i b: %s" % ("index", wartosc)) # TypeError: %i format: a real number is required, not str

nowe_imie = imiona  # kopia referencji
print(imiona)  # ['Jan', 'Piotr', 'Anna', 'Michał']
print(nowe_imie)  # ['Jan', 'Piotr', 'Anna', 'Michał']

print(id(imiona))  # 2101156433856
print(id(nowe_imie))  # 2101156433856

nowa_lista = imiona.copy()
print(id(nowa_lista))  # 2101158276480

imiona.clear()  # usunie elemnty z listy
print(imiona)  # []
print(nowe_imie)  # []

nowe_imie.append("Radek")
print(imiona)  # ['Radek']
print(nowe_imie)  # ['Radek']

pimie = imiona[:]
qimie = list(imiona)
print(id(pimie))  # 2103135052224
print(id(qimie))  # 2103172283456
print(id(imiona))  # 2103132868544

# krotka - tupla
# kolekcja niemutowalna
# tylko do odczytu
# pozwala lepiej zarządzzać pamięcią
# miasto = "Kraków", "Lublin", "Płock", "Łódź"
miasto = ("Kraków", "Lublin", "Płock", "Łódź")
print(miasto)
print(type(miasto))
# ('Kraków', 'Lublin', 'Płock', 'Łódź')
# <class 'tuple'>

krotka_jeden = ("radek",)  # pep8 tak zaleca
print(type(krotka_jeden))
print(krotka_jeden)  # ('radek',)

print(miasto.index("Łódź"))  # index numer 3
print(miasto.count(("Łódź")))  # wystepuje 1 raz

# del miasto[0] # TypeError: 'tuple' object doesn't support item deletion

del miasto
# print(miasto) # NameError: name 'miasto' is not defined

# zbiór, set
# nie zachowuje kolejnosci (brak indeksu)
# nie ma duplikatów
# hashowane

drzewa = {'jodła', 'buk', "świerk", 'dąb', 'klon'}
print(drzewa)  # {'dąb', 'buk', 'klon', 'świerk', 'jodła'}
print(type(drzewa))  # <class 'set'>

drzewa.add("osika")
drzewa.add("osika")
drzewa.add("osika")
drzewa.add("osika")
print(drzewa)  # {'buk', 'dąb', 'jodła', 'klon', 'świerk', 'osika'}

# pusty zbior
pusty_zbior = set()  # tylko i wyłacznie za pomocą set()
print(pusty_zbior)  # set()

lista = [1, 2, 3, 4, 4, 7, 7, 6, 5, 1, 2, 3]
zbior = set(lista)
print(zbior)  # {1, 2, 3, 4, 5, 6, 7} bez zachowannia kolejności

# słownik - para klucz:wartosc
# {"name" : "John", 'age':30, "car: None}
# odpowiednik jsona
# {"name":"John", "age":30, "car":null}

pusty_slownik = {}  # {1, 2, 3, 4, 5, 6, 7}
print(type(pusty_slownik))  # <class 'dict'>

pusty_slownik = dict()
print(type(pusty_slownik))
print(pusty_slownik)  # {}

osoba = {
    "id": 89,
    'imie': "Tadeusz",
    "rok": 1976,
    "miasto": "Łódź"
}

print(osoba)  # {'id': 89, 'imie': 'Tadeusz', 'rok': 1976, 'miasto': 'Łódź'}
print(type(osoba))  # <class 'dict'>

print(osoba['miasto'])  # Łódź
# print(osoba['Miasto'])  # KeyError: 'Miasto'

print(osoba.get('miasto'))  # Łódź
print(osoba.get('Miasto'))  # None
print(osoba.get("Miasto", "default"))  # default

osoba['imie'] = "Radek"
print(osoba)  # {'id': 89, 'imie': 'Radek', 'rok': 1976, 'miasto': 'Łódź'}

print(osoba.keys())
print(osoba.values())
print(osoba.items())

# dict_keys(['id', 'imie', 'rok', 'miasto'])
# dict_values([89, 'Radek', 1976, 'Łódź'])
# dict_items([('id', 89), ('imie', 'Radek'), ('rok', 1976), ('miasto', 'Łódź')])

lista = [1, 2, 3, 4, 4, 7, 7, 6, 5, 1, 2, 3]

print(dict.fromkeys(lista))
# {1: None, 2: None, 3: None, 4: None, 7: None, 6: None, 5: None}
print(list(dict.fromkeys(lista)))  # [1, 2, 3, 4, 7, 6, 5] nie zmienia kolejnosci

# pętla - while - sterowana warunkiem

licznik = 0
while True:
    print("Dane")
    licznik += 1
    if licznik > 10:
        break  # przerywa pętlę

print(50 * "-")  # --------------------------------------------------
licznik = 0
while licznik < 10:
    licznik += 1
    print("Licznik dane 2")
# Dane
# --------------------------------------------------
# Licznik dane 2

przekaski = ['hotdog', 'pizza', 'hamburger', 'frytki']
prompt = "Wybierz swoją przekąskę"

# while True:
#     choice = input(prompt.strip()) # strip() - usuniecie białych znaków
#
#     if choice in przekaski:
#         break
#     print('Nie ma')
#
# Wybierz swoją przekąskęzupa
# Nie ma
# Wybierz swoją przekąskękola
# Nie ma
# Wybierz swoją przekąskęfrytki

# walrus operator, operator morsa
# :=
#
# while (choice := input(prompt)) not in przekaski:
#     print("Nie ma")
# Wybierz swoją przekąskęzupa
# Nie ma
# Wybierz swoją przekąskęfrytki

# zmienna, wpisac wwyraz
# obliczyc długossc
# w zaleznosci od długosci wypisac tekst, wypisac ile wybosi ta długosc
# uzyc walrus operatora

wyraz = input("Wpisz wyraz: ")

if (n := len(wyraz)) < 5:
    print(f"Wyraz jest krótki. Ma długość {n} znaków.")
elif n <= 8:
    print(f"Wyraz ma średnią długosc. Ma długość {n} znaków.")
else:
    print(f"Wyraz jest długi. Ma długość {n} znaków.")
# Wpisz wyraz: Radek
# Wyraz ma średnią długosc. Ma długość 5 znaków.
