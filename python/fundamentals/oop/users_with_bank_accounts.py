

class BankAccount:

    def __innit__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            self.balance -= 5
            print("insufficient funds")
            return self
        else: 
            self.balance -= amount
            return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * 1.01
            return self





class User:		
    def __init__(self, first_name, last_name, e_mail, age):
        self.first_name = first_name
        self.last_name = last_name
        self.e_mail = e_mail
        self.age = age
        self.account = BankAccount(0.02, 0)

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.e_mail)
        print(self.age)
        print(self.account.balance)
        return self
        


harrison = User("Harrison", "Anthony", "harrisoneanthony@gmail.com", 32)
hayley = User("Hayley", "Finik", "hfinik@nobull.com", 26)
bella = User("Bella", "Alzendez", "bella.@dog.com", 3)


harrison.display_info()