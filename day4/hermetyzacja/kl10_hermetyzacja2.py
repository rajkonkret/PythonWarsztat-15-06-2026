class Car:
    """
    Klasa opisujaca samochód
    """

    def __init__(self, model):
        self.__model = model

    @property
    def model(self):
        """
        Getter - umożliwia odczyt pola
        :return:
        """
        print("Wypisuje model")
        return self.__model


car = Car("BMW")
print(car.model)  # BMW, Wypisuje model, uzywanie metody model

# mozna dodawac pola poza klasa
car.name = "Radek"
print(car.name)  # Radek
