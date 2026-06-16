import time


def wznowienie(n, k):
    print("Wstrzymanie dziłania...")
    yield 1001  # odeslij dane, wstrzymaj działanie

    print("Wznowienie działania")

    print("Działanie - dodawanie - wstrzymane")
    yield n + k

    print("Wznowienie działania")
    n = 3 * n
    yield n - k

    print("Wznowienie działania - mnozenie")
    yield n * k

    print("Wznowienie działania - dzielenie")
    yield n / k


print(20 * "--")
for i in wznowienie(6, 8):
    if i == 1001:
        continue  # pomija kolejne linie, bierze nastepny element w pętli
    time.sleep(1)
    print(f"Yield zwraca wartość: {i}")

# ----------------------------------------
# Wstrzymanie dziłania...
# Yield zwraca wartość: 1001 - przy continue nie pojawi się ta wartość
# Wznowienie działania
# Działanie - dodawanie - wstrzymane
# Yield zwraca wartość: 14
# Wznowienie działania
# Yield zwraca wartość: 10
# Wznowienie działania - mnozenie
# Yield zwraca wartość: 144
# Wznowienie działania - dzielenie
# Yield zwraca wartość: 2.25

print(20 * "-")


def gen4():
    i = 1
    while True:
        yield i * i
        i += 1


generator4 = gen4()
print(next(generator4))
print(next(generator4))
print(next(generator4))
print(next(generator4))
print(next(generator4))


def gen5():
    i = 1
    while True:
        command = yield i * i
        print(command)  # None, OK
        if command == "OK":
            print("Jestem generatorem")
        elif command == "stop":
            break  # zatrzymanie generatora
        i += 1


g5 = gen5()
print(next(g5))
print(next(g5))
print(next(g5))
g5.send("OK")
try:
    g5.send("stop")  # stop, StopIteration
except StopIteration:
    print("Koniec danych")
except Exception as e:
    print("bład:", e)

# Koniec danych

g5.close()  # zatrzymanie generatora, wskazanie do gc by usunął


def fibo_with_index(n):
    a, b = 0, 1
    for ind in range(n):
        yield ind, a
        a, b = b, a + b


fib = fibo_with_index(10)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
# (0, 0)
# (1, 1)
# (2, 1)
# (3, 2)

for i, n in fibo_with_index(5):
    print(f"Pozycja: {i}, element: {n}")
# Pozycja: 0, element: 0
# Pozycja: 1, element: 1
# Pozycja: 2, element: 1
# Pozycja: 3, element: 2
# Pozycja: 4, element: 3
