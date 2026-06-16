# napisac dekorator mierzący czas wykonania funkcji
# time.time()
# time.perf_counter()
import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        execution_time = time.perf_counter() - start_time

        print(f"Czas wykonania funkcji: {func.__name__}: {execution_time}")

        return result

    return wrapper


lista1 = list(range(10_000_000))
lista2 = list(range(10_000_000))


@measure_time
def my_time():
    time.sleep(2)


@measure_time
def add_with_for():
    result = []
    for i in range(len(lista1)):
        suma = lista1[i] + lista2[i]
        result.append(suma)
    return "OK For"


@measure_time
def add_lc():
    result = [lista1[i] + lista2[i] for i in lista1]
    return "OK LC"


@measure_time
def add_zip():
    result = [a + b for a, b in zip(lista1, lista2)]
    return "OK ZIP"


my_time()  # Czas wykonania funkcji: my_time: 2.0009553999989294
add_with_for()  # Czas wykonania funkcji: add_with_for: 2.68576409999514, Czas wykonania funkcji: add_with_for: 1.5666790999821387
add_lc()  # Czas wykonania funkcji: add_lc: 1.2878811999689788
add_zip()  # Czas wykonania funkcji: add_zip: 1.2108676999923773
