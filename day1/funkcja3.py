# lambda - skrócony zapis funkcji
# lambda zawsze zwraca wynik
# funkcja anonimowa - nie ma nazwy, mozliwosc wykonania w miejscu deklaracji

def oblicz_rabat(cena, procent):
    return cena * procent / 100

print(oblicz_rabat(500, 20)) # 100.0
