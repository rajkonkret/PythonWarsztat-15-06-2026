# klasy - element programowania obiektowego
# szablon, przepis
# cech(zmienne)
# metody (funkcja)
# obiekt kalsy (instancja)
# metoda inicjalizującą __init__ - konstruktor
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja
import math


# PascalCase, UpperCamelCase
class MyFirstClass:
    """
    klasa w Pythonie
    """

    def __init__(self, x=0, y=0):
        """
        Metoda inicjalizująca (konstruktor)
        :param x:
        :param y:
        """
        # self - obiekt
        # self.x = x
        # self.y = y
        self.move(x, y)

    # move(x, y)
    def move(self, x: int, y: int) -> None:
        """
        Zmienia x i y obiektu na nowe waartości
        :param x:
        :param y:
        :return:
        """
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate(self, other: "MyFirstClass") -> float:
        """
        For a two dimensional point (x, y), this
        is equivalent to computing the hypotenuse of a right triangle using the Pythagorean theorem, sqrt(x*x + y*y).
        :param other:
        :return:
        """
        return math.hypot(self.x - other.x, self.y - other.y)

    # metoda opisowa obiektu
    def __str__(self):
        return f"{self.x, self.y}"

    def __repr__(self):
        return f"{self.__class__.__name__}{self.x, self.y}"


ob = MyFirstClass()
print(ob)  # <__main__.MyFirstClass object at 0x000001DC7FA7CC20>
print(MyFirstClass.__doc__)
# pydoc -b - serwer
# pydoc -w .\kl1.py - plik html z dokumentacją

print(ob.x)
print(ob.y)
print(ob)  # (0, 0) po nadpisaniu __str__

point1 = MyFirstClass(5, 9)
print(point1)  # (5, 9)

point1.move(56, 90)
print(point1)  # (56, 90)

# reset()
point1.reset()
print(point1)  # (0, 0)

point2 = MyFirstClass(56, 90)
# odległość pomiędzy tymi punktami
print(point2)  # (56, 90)

print(point1.calculate(point2))
# 106.0

point3 = MyFirstClass(43, 21)
point4 = MyFirstClass(34, 78)

print(point3)  # (43, 21)
print(point4)  # (34, 78)

lista = [point1, point2, point3, point4]

print(lista)
# [<__main__.MyFirstClass object at 0x0000024B1A1BA5D0>,
# <__main__.MyFirstClass object at 0x0000024B1A3B1BD0>,
# <__main__.MyFirstClass object at 0x0000024B11AADCD0>,
# <__main__.MyFirstClass object at 0x0000024B1A20DA70>]

# __str__ -> bezposredni print(), str()

# __repr__ - reprezentacja obiektu dla programisty
# [MyFirstClass(0, 0),
# MyFirstClass(56, 90),
# MyFirstClass(43, 21),
# MyFirstClass(34, 78)]
