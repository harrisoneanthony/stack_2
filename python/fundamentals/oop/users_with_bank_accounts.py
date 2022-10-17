class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawl(self, amount):
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

    def transfer_money(self, amount, other_user):
        self.balance -= amount
        other_user.balance += amount
        self.display_user_balance()
        other_user.display_user_balance()

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            return self

class User:		
    def __init__(self, first_name, last_name, e_mail, age):
        self.first_name = first_name
        self.last_name = last_name
        self.e_mail = e_mail
        self.age = age
        self.account = BankAccount(0.4, 0)

    def display_info(self):
        self.account.display_account_info()
        print(self.account.display_account_info)
        return self
        
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawl(self, amount):
        self.account.withdrawl(amount)
        return self

    def display_user_balance(self):
        print(f"Balance: ${self.account.balance}")
        return self

    def transfer(self, amount, receiver):
        self.make_withdrawl(amount)
        receiver.make_deposit(amount)
        return self
    



harrison = User("Harrison", "Anthony", "harrisoneanthony@gmail.com", 32)
hayley = User("Hayley", "Finik", "hfinik@nobull.com", 26)
bella = User("Bella", "Alzendez", "bella.@dog.com", 3)


harrison.make_deposit(100).transfer(10, bella)

print(harrison.display_user_balance())