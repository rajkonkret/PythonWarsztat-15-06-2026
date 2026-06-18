# classmethod

class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    # zamiennik przeciążania konstruktorów
    @classmethod
    def z_pelnej_nazwy(cls, nazwa_pelna):
        imie, nazwisko = nazwa_pelna.split()
        return cls(imie, nazwisko)


osoba1 = Osoba("Jan", "Kowalski")
print(osoba1.imie, osoba1.nazwisko)
# Jan Kowalski
dane = "Jan Kowalski"
print(dane.split())  # ['Jan', 'Kowalski']
print(dane)
name, surname = dane.split()
osoba2 = Osoba(name, surname)
print(osoba2.imie)  # Jan

osoba3 = Osoba.z_pelnej_nazwy(dane)
print(osoba3.imie)
print(osoba3.nazwisko)
# Jan
# Kowalski
