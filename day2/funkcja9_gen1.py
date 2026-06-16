# generator - generuje wartosci w momencie kiedy są potrzebne
# lazy
# pozwalają oszczędzic pamięc
import time


def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


def kwadrat_gen(n):
    for x in range(n):
        yield x ** 2  # pamięta gdzie zakończył, zatrzymuje działanie po kolejnym elemencie, zwraca aktualny wynik działania


kwa = kwadrat_gen(10)
print(kwa)  # <generator object kwadrat_gen at 0x000001F7B15A8EE0>

# next() - wypisz kolejny element z danych
print(next(kwa))
print(next(kwa))
print(next(kwa))
print(next(kwa))

print("zrób cokolwiek")
print("wykonaj zadanie...")

print(next(kwa))
print(type(kwa))  # <class 'generator'>

print(next(kwa))  # 25
print(next(kwa))  # 25
print(next(kwa))  # 25
print(next(kwa))  # 25
print(next(kwa))  # 25

# dane zostały wyczerpane
# print(next(kwa))  # StopIteration

kwa2 = kwadrat_gen(10)

for k in kwa2:
    print(k)
    print("Przetwarzam dane...")
    time.sleep(2)
# 81
# Przetwarzam dane...

kwa3 = kwadrat_gen(5)
kwa4 = kwadrat_gen(5)

print(next(kwa3))
print(next(kwa3))
print(next(kwa3))

print(next(kwa4))
print(next(kwa4))
print(next(kwa4))

print(next(kwa3)) # 9