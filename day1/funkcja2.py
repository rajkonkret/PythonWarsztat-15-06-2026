# funkcja zagniezdzona, funkcja wewnętrzna
# dekorator - @funkcja - wykorzystuje idee funkcji wewnętrznej

def przygotuj_powiadomienie(klient):
    print(f"Przygotowuję system powiadomien dla klienta: {klient}")

    def wysli_powiadomienie():
        print(f'Wysyłąm powiadomienie do klienta: {klient}')

    # wysli_powiadomienie()
    return wysli_powiadomienie  # adres funkcji (referencja)


powiadomienie_anny = przygotuj_powiadomienie("Anna")
print(powiadomienie_anny)  # <function przygotuj_powiadomienie.<locals>.wysli_powiadomienie at 0x00000276576B3270>
print(type(powiadomienie_anny))  # <class 'function'>

powiadomienie_anny()
powiadomienie_anny()
powiadomienie_anny()
powiadomienie_anny()


# Wysyłąm powiadomienie do klienta: Anna
# Wysyłąm powiadomienie do klienta: Anna
# Wysyłąm powiadomienie do klienta: Anna
# Wysyłąm powiadomienie do klienta: Anna

# zrobic funkcję plik()
# funkcja przyjmuje parametr:  zapis, odczyt
# w zaleznosci od parametru ma zwrocic odpowiednią funkcję
# uzyc odczyt, zapis

def plik(arg):
    print("Sprawdzam dysk...")

    def zapis(dane):
        print(f"Zapis danych do pliku... {dane}")

    def odczyt():
        return "Odczytane dane z pliku..."

    if arg.casefold() == "zapis":
        return zapis
    else:
        return odczyt  # zwraca referencję


zapis_plik = plik("zapis")

# zapis_plik()# TypeError: plik.<locals>.zapis() missing 1 required positional argument: 'dane'
zapis_plik("moje dane")
# Zapis danych do pliku... moje dane

odczyt_pliku = plik("odczyt")
dane = odczyt_pliku()
print("Odczytane dane:", dane)
# Odczytane dane: Odczytane dane z pliku...

fh = open("test.txt", "w")
fh.write("Zapisane\n")
fh.close()

# domknięcie
# funkcja wewnętrzna pamięta wartośc przekazene w funkcji zewnętrznej
def obsluga_zamowienia(numer_zamowienia):
    status = "nowe"

    def zmien_status(nowy_status):
        nonlocal status # by działło domknięcie

        poprzedni_status = status
        status = nowy_status

        print(f"""
Zamówienie {numer_zamowienia}:
{poprzedni_status} -> {status}
""")

    return zmien_status

zamowienie_1001 = obsluga_zamowienia(1001)

zamowienie_1001("opłacone")
zamowienie_1001("spakowane")
zamowienie_1001("wysłane")
zamowienie_1001("dostarczone")
#
# Zamówienie 1001:
# nowe -> opłacone
#
#
# Zamówienie 1001:
# opłacone -> spakowane
#
#
# Zamówienie 1001:
# spakowane -> wysłane
#
#
# Zamówienie 1001:
# wysłane -> dostarczone
#


