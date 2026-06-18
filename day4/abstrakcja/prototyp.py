# klasa abstrakcyjna
# posiada metodoty abstrakcyjne
# nie można tworzyc obiektów tej klasy
from abc import ABC, abstractmethod


class Prototyp(ABC):
    """
    Klasa abstrakcyjna
    """

    def __init__(self, x):
        self.x = x

    @abstractmethod
    def policz(self):
        pass

    @abstractmethod
    def info(self):
        pass

    def msg(self):
        print("Metoda nieabstrakcyjna klasy abstrakcyjnej")
