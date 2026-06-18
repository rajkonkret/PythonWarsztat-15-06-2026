# hermetyzacja - ukrywanie pól
# enkapsulacja - ukrywanie pól i wystawianie metod do odczytu i zapisu tych pół (gettery, settery)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        # name mangling
        # private - pole prywatne
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")


if __name__ == '__main__':
    account = BankAccount("Radek", 2500)

    # print(account.__balance)  # 2500, AttributeError: 'BankAccount' object has no attribute '__balance'. Did you mean: 'get_balance'?

    print(account.get_balance())  # 2500
