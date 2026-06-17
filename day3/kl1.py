# klasy - element programowania obiektowego
# szablon, przepis
# cech(zmienne)
# metody (funkcja)
# obiekt kalsy (instancja)
# metoda inicjalizującą __init__ - konstruktor
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja

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
    def move(self, x, y):
        """
        Zmienia x i y obiektu na nowe waartości
        :param x:
        :param y:
        :return:
        """
        self.x = x
        self.y = y

    # metoda opisowa obiektu
    def __str__(self):
        return f"{self.x, self.y}"


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
