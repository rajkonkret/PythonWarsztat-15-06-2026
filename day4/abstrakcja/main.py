# from prototyp import Prototyp

# prototyp = Prototyp(1)
# TypeError: Can't instantiate abstract class Prototyp without an implementation for abstract methods 'info', 'policz'

# uzyc xyz w main
# dorobic klase dziedziczaca po Protyp

from xyz import XYZ
from regular import Regular

xyz1 = XYZ(1, 2, 3)
print(xyz1.info("xyz 001"))
print(f"Policz: {xyz1.policz()}")
# xyz 001xyz 001xyz 001
# Policz: 5

xyz1.msg()  # Metoda nieabstrakcyjna klasy abstrakcyjnej

reg1 = Regular(4, 5)
print(reg1.info("rg 002"))
print(f"Policz: {reg1.policz()}")
# Wiadomość: rg 002
# Policz: 3.2

reg1.msg()
xyz1.msg()
# Metoda nieabstrakcyjna klasy abstrakcyjnej
# Metoda nieabstrakcyjna klasy abstrakcyjnej

lista = [reg1, xyz1]  # obiekty różnych klas

# polimorfizm
# obiekty róznych kals traktujemy jako obiekty jedej klasy (abstrakcyjne)
for i in lista:
    print(i.policz())
# 3.2
# 5
