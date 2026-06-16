# dekorator - funkcja, która przyjmuje inną funkcję jako argument
# wykorzystuje mechanizm funkcji wew

def dekor(func):
    def wew():
        print("Dekorator. dodatkowy wynik")
        return func()

    return wew  # zwracamy adres funkcji

@dekor
def nasza_funkcja():
    print("Funkcja, którą chcemy udekorowac")


nasza_funkcja()
# Funkcja, którą chcemy udekorowac

# po uzyciu dekoratora:
# Dekorator. dodatkowy wynik
# Funkcja, którą chcemy udekorowac