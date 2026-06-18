# iterator
# lazy, dane tylko gdy potrzebne

lista = [1, 2, 3, 4, 5]
iterator = iter(lista)
print(next(iterator))
print(next(iterator))
print(next(iterator))

print("Cos innego")
print(next(iterator))


class Count:
    def __init__(self, lows, high):
        """

        :param lows:
        :param high:
        """
        self.current = lows
        self.highs = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.highs:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


print(25 * "-")
counter = Count(1, 5)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
print(next(counter))  # 4
print(next(counter))  # 5
try:
    print(next(counter))  # StopIteration
except StopIteration as e:
    print("Koniec:", e)
