# zrobic metode zwracająca elementy spełniajace warunek search(name)

class ContactList(list['Contact']):

    def search(self, name):
        matching_contacts = []
        for c in self:
            if name.casefold().strip() in c.name.casefold().strip():
                matching_contacts.append(c)

        return matching_contacts


cl = ContactList()
cl.append("Radek")


# print(cl.search("Radek"))

class Contact:
    """
    Klasa contact - stworzony obiekt ma automatycznie trafiac do wspolnej listy w tej klasie
    """
    # all_contacts = []  # wspolna lista dla wszystkich obiektów tej klasy
    all_contacts = ContactList()  # wspolna lista dla wszystkich obiektów tej klasy
    x = 'TEST'

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

print(c1.x)  # TEST
print(Contact.x)  # TEST
c2.x = 'TEST2'

print(Contact.x)  # TEST
print(c2.x)  # TEST2
print(c1.x)  # TEST


class Suplier(Contact):
    """
    Klasa dziedziczy po klasie Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


sup1 = Suplier("Marek", "marek@wp.pl")
print(sup1)  # Marek marek@wp.pl
print(sup1.all_contacts)
# [Radek radek@wp.pl, Tomek tomek@wp.pl, Anna anna@wp.pl, Marek marek@wp.pl]

sup1.order("kawa")  # kawa zamówiono od Marek

print(Contact.all_contacts)  # [Radek radek@wp.pl, Tomek tomek@wp.pl, Anna anna@wp.pl, Marek marek@wp.pl]
print(Contact.all_contacts.search("Radek"))  # [Radek radek@wp.pl]

osoba = Contact.all_contacts.search("Radek")
for i in osoba:
    print(i)
    print(i.name)
    print(i.email)


# Radek radek@wp.pl
# Radek
# radek@wp.pl

# zrobic klase Friend dziedzicząca po Suplier ale pozwaljącą dodac do Friend nr telefonu

class Friend(Suplier):
    """
    Klasa dziedziczy po klasie Suplier
    """

    def __init__(self, name, email, phone="000000000"):
        super().__init__(name, email)  # super() klasa nadrzędna, musimy wywołąć metode __init__
        self.phone = phone

    def __repr__(self):
        return f"{self.name} {self.email} +48{self.phone}"


f1 = Friend("MArk", "mark@gov.pl")
f2 = Friend("Kamil", "kamil_the_best@gov.pl", "500600700")

print(f1, f2)  # MArk mark@gov.pl +48000000000 Kamil kamil_the_best@gov.pl +48500600700

print(Contact.all_contacts)
# [Radek radek@wp.pl, Tomek tomek@wp.pl, Anna anna@wp.pl,
# Marek marek@wp.pl, MArk mark@gov.pl +48000000000, Kamil kamil_the_best@gov.pl +48500600700]

from pprint import pprint

pprint(Contact.all_contacts)
# [Radek radek@wp.pl,
#  Tomek tomek@wp.pl,
#  Anna anna@wp.pl,
#  Marek marek@wp.pl,
#  MArk mark@gov.pl +48000000000,
#  Kamil kamil_the_best@gov.pl +48500600700]


# kolejność rozwiązywania nazw metod (pól) dla obiektu
print(Friend.__mro__)
# (<class '__main__.Friend'>, <class '__main__.Suplier'>, <class '__main__.Contact'>, <class 'object'>)