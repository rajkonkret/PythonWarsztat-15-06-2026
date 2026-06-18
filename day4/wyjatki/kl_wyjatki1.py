# print(2 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonWarsztat-15-06-2026\day4\wyjatki\kl_wyjatki1.py", line 1, in <module>
#     print(2/0)
#           ~^~
# ZeroDivisionError: division by zero
#
# Process finished with exit code 1

# raise ZeroDivisionError("Bład dzielenia")
# C:\Users\CSComarch\PycharmProjects\PythonWarsztat-15-06-2026\.venv\Scripts\python.exe C:\Users\CSComarch\PycharmProjects\PythonWarsztat-15-06-2026\day4\wyjatki\kl_wyjatki1.py
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonWarsztat-15-06-2026\day4\wyjatki\kl_wyjatki1.py", line 10, in <module>
#     raise ZeroDivisionError("Bład dzielenia")
# ZeroDivisionError: Bład dzielenia
#
# Process finished with exit code 1

class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    x = int(input("Podaj liczbę całkowitą większą od zera:"))
    if x <= 0:
        raise MyException("Liczba musi być wieksza od zera")
except MyException as e:
    print("Wartość musi być większa od zera")
except ValueError as e:
    print("Błąd wartości:", e)
except Exception as e:
    print("Bład:", e)
else:  # tylko gdy nie ma błedu
    print("Działanie na x:", x * 2)
finally:  # wykona się zawsze
    print("koniec")
