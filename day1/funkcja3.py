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

# map() - mapowanie danych
# funkcja wyzszego rzędu - jako argument przyjmuje inna funkcję

# lamda jako funkcja anonimowa
print(f"Lambda: {list(map(lambda cena: round(cena * 1.23, 2), ceny_netto))}")
# Lambda: [123.0, 307.5, 98.4, 1476.0, 55.35]
