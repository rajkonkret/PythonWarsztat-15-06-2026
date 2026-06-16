# funkcja rekurencyjna
# funkcja wywołuje sama siebie
from functools import lru_cache

from mypyc.irbuild.vec import vec_to_list


def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)


print(silnia(5))  # 120


def nwd(a, b):
    if b == 0:
        return a
    return nwd(b, a % b)  # % - modulo, reszta z dzielenia


print(nwd(48, 18))  # 6


@lru_cache(maxsize=512)
def fibonacci(n):
    if n < 0:
        raise ValueError("n nie może być ujemne")

    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
print(fibonacci.cache_info())
# CacheInfo(hits=3, misses=6, maxsize=512, currsize=6)
print(fibonacci(10))
print(fibonacci.cache_info())
# CacheInfo(hits=9, misses=11, maxsize=512, currsize=11)

# zsumowac wszystkie wartosci ze słownika
nested_data = {
    "a": 1,
    "b": {
        "c": 2,
        "d": [3, 4, {"e": 5}]
    },
    "f": [6, 7]
}


def sum_nested(data):
    total = 0

    if isinstance(data, dict):
        for key, value in data.items():
            total += sum_nested(value)
    elif isinstance(data, list):
        for item in data:
            total += sum_nested(item)
    elif isinstance(data, (int, float)):
        total += data

    return total


result = sum_nested(nested_data)
print("Sum nested is:", result) # Sum nested is: 28
