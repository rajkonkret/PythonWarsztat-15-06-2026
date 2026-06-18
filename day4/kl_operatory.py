from functools import total_ordering


class MyNumber:
    def __init__(self, value):
        self.value = value


num1 = MyNumber(1)
num2 = MyNumber(15)

# print(num1 < num2)  # TypeError: '<' not supported between instances of 'MyNumber' and 'MyNumber'
print(num1.value < num2.value)  # True


# __eq__, __ne__
# i jedna z pozostałych __lt__ to __le__ to __gt__ to __ge__
@total_ordering
class MyNumber2:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


num3 = MyNumber2(1)
num4 = MyNumber2(15)
print(num3 < num4)  # True

print(num3 == num4)  # False
num5 = MyNumber2(15)
print(num4 == num5)  # True
print(num5 > num3)  # True
