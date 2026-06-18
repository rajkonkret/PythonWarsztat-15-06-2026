# starsze podejście
class Obliczanie:
    """
    starsze podejscie - metoda statyczna
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def oblicz(x, y, z):
        return (x + y) * z


Obliczanie.oblicz = staticmethod(Obliczanie.oblicz)
