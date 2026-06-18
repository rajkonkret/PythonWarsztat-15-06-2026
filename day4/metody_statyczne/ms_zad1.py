# metoda statyczna - nie potrzebuja obiektu klasy

class Matematyka:

    # def dodaj(self, a, b):
    #     return a + b

    @staticmethod
    def dodaj(a, b):
        return a + b

    @staticmethod
    def odejmij(a, b):
        return a - b


# kalk = Matematyka()
# print(kalk.dodaj(56, 90))  # 146

print(Matematyka.dodaj(5, 90))  # 95

print(Matematyka.odejmij(90, 78))  # 12
