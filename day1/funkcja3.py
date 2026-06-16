# lambda - skrócony zapis funkcji
# lambda zawsze zwraca wynik
# funkcja anonimowa - nie ma nazwy, mozliwosc wykonania w miejscu deklaracji
from functools import reduce


def oblicz_rabat(cena, procent):
    return cena * procent / 100


print(oblicz_rabat(500, 20))  # 100.0

oblicz_rabat_lambda = lambda cena, procent: cena * procent / 100
print(oblicz_rabat_lambda(500, 200))  # 1000.0

# lambda jako funkcja anonimowa
wynik = (lambda cena, rabat: cena - cena * rabat)(200, 0.15)
print(wynik)  # 170.0

# mapowania
ceny_netto = [100, 250, 80, 1200, 45]
# oblicz ceny jako brutto. vat=23%

ceny_brutto = []

for cena in ceny_netto:
    ceny_brutto.append(round(cena * 1.23, 2))

print(ceny_brutto)  # [123.0, 307.5, 98.4, 1476.0, 55.35]

# list comprehensions
ceny_brutto = [round(cena * 1.23, 2) for cena in ceny_netto]
print(ceny_brutto)  # [123.0, 307.5, 98.4, 1476.0, 55.35]


def dodaj_vat(cena):
    return round(cena * 1.23, 2)


for cena in ceny_netto:
    ceny_brutto.append(dodaj_vat(cena))

print(ceny_brutto)
# [123.0, 307.5, 98.4, 1476.0, 55.35, 123.0, 307.5, 98.4, 1476.0, 55.35]

ceny_brutto_map = list(map(dodaj_vat, ceny_netto))
print(ceny_brutto_map)  # [123.0, 307.5, 98.4, 1476.0, 55.35]

# map() - mapowanie danych, jest lazy
# funkcja wyzszego rzędu - jako argument przyjmuje inna funkcję

# lamda jako funkcja anonimowa
print(f"Lambda: {list(map(lambda cena: round(cena * 1.23, 2), ceny_netto))}")
# Lambda: [123.0, 307.5, 98.4, 1476.0, 55.35]

ceny = [100, 200, 300]
rabaty = [0.10, 0.20, 0.05]

cena_po_rabacie = list(
    map(lambda cena, rabat: cena * (1 - rabat), ceny, rabaty)
)
print(cena_po_rabacie)  # [90.0, 160.0, 285.0]

# filtrowanie
temperatury = [-12, -2, 0, 4, 15, 22, 31, 38, 38]
# wyfiltrowaac do listy upalne, większe niz 30

upalne_dni = []

for temperatura in temperatury:
    if temperatura >= 30:
        upalne_dni.append(temperatura)

print(upalne_dni)  # [31, 38, 38]

# filter() - zwraca elementy spełniające warunek
upalne_dni = list(
    filter(lambda temperatura: temperatura >= 30, temperatury)
)

print(upalne_dni)  # [31, 38, 38]

# > 10 , < 25

umiarkowane = list(
    filter(lambda temperatura: 10 <= temperatura <= 25, temperatury)
)

print(umiarkowane)  # [15, 22]

# zrobic liste złożoną ze str
# przefiltrowac dłuzsze niz 6
# za pomoca filter i list comprehensions

miasta = [
    'Warszawa',
    "Kraków",
    "Łódź",
    "Katowice",
    "Wrocław",
    "Gdańsk"
]

dlugie_nazwy = list(
    filter(lambda miasto: len(miasto) >= 6, miasta)
)

print(dlugie_nazwy)  # ['Warszawa', 'Kraków', 'Katowice', 'Wrocław', 'Gdańsk']

dlugie_nazwy = [miasto for miasto in miasta if len(miasto) >= 6]
print(dlugie_nazwy)  # ['Warszawa', 'Kraków', 'Katowice', 'Wrocław', 'Gdańsk']

# wybrac ceny wikesze niz 100, obnizyc o 10 %

ceny = [150, 250, 80, 75]

wieksze_100 = list(
    filter(lambda cena: cena > 100, ceny)
)
print(wieksze_100)  # [150, 250]

rabat_10 = list(
    map(lambda cena: cena * 0.9, wieksze_100)
)

print(rabat_10)  # [135.0, 225.0]

pracownicy = [
    {"imie": "Anna", "pensja": 7500, "wiek": 32},
    {"imie": "Radek", "pensja": 17500, "wiek": 41},
    {"imie": "Tomek", "pensja": 6500, "wiek": 29},
    {"imie": "Marek", "pensja": 12000, "wiek": 35},
]

# pracownik z najwyższą pensją

# max()
najlepeij_oplacany = max(
    pracownicy,
    key=lambda osoba: osoba['pensja']
)

print(najlepeij_oplacany)  # {'imie': 'Radek', 'pensja': 17500, 'wiek': 41}

# najmłodszy pracownik
# min()
najmlodszy = min(
    pracownicy,
    key=lambda osoba: osoba['wiek']
)

print(najmlodszy)  # {'imie': 'Tomek', 'pensja': 6500, 'wiek': 29}

# sorted()
posortowani = sorted(
    pracownicy,
    key=lambda osoba: osoba['pensja']
)

print(posortowani)

posortowani = sorted(
    pracownicy,
    key=lambda osoba: osoba['pensja'],
    reverse=True
)

print(posortowani)

# minus(-) - oznacza sortuj malejąco
posortowani = sorted(
    pracownicy,
    key=lambda osoba: (-osoba['pensja'], osoba['wiek'])

)

print(posortowani)

# itemgetter
from operator import itemgetter

posortowani = sorted(
    pracownicy,
    key=itemgetter("pensja")  # odpowiednik: lambda osoba: osoba['pensja']
)
print(posortowani)

# uzupełnienie danych

# setdefault()

klient1 = {
    "imie": "Anna",
    "miasto": "Kraków"
}

klient2 = {
    "imie": "Radek",
    "miasto": "Gdańsk",
    "telefon": "500-600-700"
}

dodaj_telefon = lambda klient: klient.setdefault(
    "telefon",
    "brak numeru"
)

print(dodaj_telefon(klient1))  # brak numeru
print(dodaj_telefon(klient2))  # 500-600-700

print(klient1)
print(klient2)
# {'imie': 'Anna', 'miasto': 'Kraków', 'telefon': 'brak numeru'}
# {'imie': 'Radek', 'miasto': 'Gdańsk', 'telefon': '500-600-700'}

# miasta i kod pocztowy
# zrobic funkcje z setdefault, zeby uzupełniło słoniki

r0 = {'miasto': 'Kielce'}
r1 = {"miasto": "Kielce", "ZIP": "25-900"}

d_zip = lambda row: row.setdefault("ZIP", "00-000")
print(d_zip(r0))
print(d_zip(r1))

print(r0)
print(r1)
# {'miasto': 'Kielce', 'ZIP': '00-000'}
# {'miasto': 'Kielce', 'ZIP': '25-900'}

# reduce()
# reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)
# bierze kolejne elementy iłączy je w jeden wynik
liczby = [1, 3, 4, 5]
wynik = reduce(
    lambda x, y: x * y,
    liczby
)

print(wynik)  # 60

zamowienia = [120, 300, 80, 500]

wynik = reduce(
    lambda wynik, wartosc: wynik + wartosc,
    zamowienia
)
print(wynik)  # 1000

# reduce(lambda x, y: x + y, [])
# TypeError: reduce() of empty iterable with no initial value
# wartość domyślna
print(reduce(lambda x, y: x + y, [], 0))  # 0

from operator import mul

liczby = [2, 3, 4]
wynik = reduce(mul, liczby)
print(wynik)  # 24
