# stworzenie ksiązki telefonicznej
# wykorzystaj pętlę while
# dodaj kontakt, usun kontakt, wyszukaj kontakt, lista kontaktow
# * obiekty

contacts = {}
while True:
    print(f"""
1. Dodaj kontakt
2. Usuń kontakt
3. Wyszukaj kontakt
4. Wyświetl listę kontaktów
5. Koniec
""")
    try:
        odp = input("Wybierz opcję")  # str

        if odp == "1":
            name = input("Podaj imię kontaktu")
            number = input("Podaj numer telefonu kontaktu(tylko cyfry):")
            if not number.isdigit():
                raise ValueError("Numer telefonu powinien zawierać cyfry")
            else:
                contacts[name.lower()] = number
                print("Kontakt został dodany")
        elif odp == "5":
            break
        else:
            print("Błędny wybór")
    except Exception as e:
        print("Bład:", e)
