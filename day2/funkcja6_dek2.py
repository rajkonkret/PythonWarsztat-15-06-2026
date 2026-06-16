# zrobic dekorator
# zamiana na małe litery, oczyszczenie z białych znaków
# wypisac wynik działania funkcji kolorem czerwonym i bold

def lowercase_decorator(func):
    def wew(*args, **kwargs):
        # *args - dowolna ilosc argumentów po pozycji 1,2,3,4
        # **kwargs - argumenty słownikowe a=10, b=12
        return func(*args, **kwargs).lower().strip()

    return wew


@lowercase_decorator
def nasza_funkcja():
    return "Hello World"


print(nasza_funkcja())  # hello world


# https://en.wikipedia.org/wiki/ANSI_escape_code
def color_decorator(func):
    def wrapper(*args, **kwargs):
        # *args - dowolna ilosc argumentów po pozycji 1,2,3,4
        # **kwargs - argumenty słownikowe a=10, b=12
        result = func(*args, **kwargs)
        return "\033[31m" + result + "\033[0m"

    return wrapper


@color_decorator
def nasza_funkcja_kolor(string):
    return f"(color) Podałeś: {string}"


print(nasza_funkcja_kolor("Test Koloru"))


# kolejnośc ma znaczenie
@color_decorator
@lowercase_decorator
def nasza_funkcja_dwa_dekoratory(string):
    return f"(color) Podałeś: {string}"


print(nasza_funkcja_dwa_dekoratory("Test dwa"))

# colorama
from colorama import Fore, Style, init

# pip install colorama

init(autoreset=True)


def czerwony_bold(func):
    def wrapper(*args, **kwargs):
        wynik = func(*args, **kwargs)

        print(
            Style.BRIGHT + Fore.RED + str(wynik) + Style.RESET_ALL
        )

        return wynik

    return wrapper

@czerwony_bold
def komunikat():
    return "Uwaga! Wystąpił bład."

komunikat()