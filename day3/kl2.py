class Contact:
    """
    Klasa contact - stworzony obiekt ma automatycznie trafiac do wspolnej listy w tej klasie
    """
    all_contacts = []  # wspolna lista dla wszystkich obiektów tej klasy

    def __init__(self, name, email):
        """

        :param name:
        :param email:
        """
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    # dopisac repr
    def __repr__(self):
        return f"{self.name} {self.email}"


c1 = Contact("Radek", "radek@wp.pl")
c2 = Contact("Tomek", "tomek@wp.pl")
c3 = Contact("Anna", "anna@wp.pl")

print(c1.all_contacts)
# [Radek radek@wp.pl, Tomek tomek@wp.pl, Anna anna@wp.pl]

# bez obiektu
print(Contact.all_contacts)  # [Radek radek@wp.pl, Tomek tomek@wp.pl, Anna anna@wp.pl]
