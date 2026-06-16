# lambda - skrócony zapis funkcji
# lambda zawsze zwraca wynik
# funkcja anonimowa - nie ma nazwy, mozliwosc wykonania w miejscu deklaracji

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
print(dlugie_nazwy)
