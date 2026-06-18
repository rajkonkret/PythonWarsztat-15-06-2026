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


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


point1 = Point(1, 4)
point2 = Point(9, 4)
print(point1 + point2)  # Point(10, 8)
