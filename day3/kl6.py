# można dziedziczyć po wielu klasach

class A:
    """
    Klasa A
    """

    def method(self):
        print("Metoda z klasy A")


a = A()
a.method()  # Metoda z klasy A


class B:
    """
    Klasa B
    """

    def method(self):
        print("Metoda z klasy B")


b = B()
b.method()  # Metoda z klasy B


# dziedziczenie po wielu klasach, kolejnośc ma znaczenie
class C(B, A):
    """
    Klasa dziedziczy po klasie B i A
    """


c = C()
c.method()  # Metoda z klasy B
print(C.__mro__)


# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

class D(A, B):
    """
    Klasa dziedziczy po klasie A i B
    """


d = D()
d.method()  # Metoda z klasy A


class E(A, B):
    def method(self):
        print("Metoda z klasy E")


e = E()
e.method()  # Metoda z klasy E
print(E.__mro__)


# (<class '__main__.E'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

class F(A, B):
    """
    Chcemy użyc metody z klasy B
    """

    def method(self):
        B.method(self)  # jawnie wskazujemy z jakiej klasy chcemy użyć metody


f = F()
f.method()  # Metoda z klasy B


class G(A, B):

    def method(self):
        super().method()  # super() klasa nadrzędna tutaj: A
        print("dopisane")
        B.method(self)


# problem dziedziczenia po wielu klasach
# class H(A, F):
#
#     def method(self):
#         super().method()  # super() klasa nadrzędna tutaj: A
#         print("dopisane")
#         B.method(self)
#
#
# # TypeError: Cannot create a consistent method resolution order (MRO) for bases A, F
# # h = H()
# print(H.__mro__)
# # TypeError: Cannot create a consistent method resolution order (MRO) for bases A, F

# kolejnośc ma znaczenie
class H(F, A):

    def method(self):
        super().method()  # super() klasa nadrzędna tutaj: A
        print("dopisane")
        B.method(self)


print(H.__mro__)
# (<class '__main__.H'>,
# <class '__main__.F'>,
# <class '__main__.A'>,
# <class '__main__.B'>,
# <class 'object'>)
