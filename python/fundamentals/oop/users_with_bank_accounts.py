

class BankAccount:

    def __init__(self, int_rate, balance):
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

    def transfer_money(self, amount, other_user):
        self.balance -= amount
        other_user.balance += amount
        self.display_user_balance()
        other_user.display_user_balance()

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance 
            return self





class User:		
    def __init__(self, first_name, last_name, e_mail, age):
        self.first_name = first_name
        self.last_name = last_name
        self.e_mail = e_mail
        self.age = age
        self.checking_account = BankAccount(0.4, 0)

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.e_mail)
        print(self.age)
        print(self.checking_account.balance)
        print(self.savings_account.balance)
        return self
        
    def make_deposit_to_checking(self, amount):
        self.checking_account.deposit(amount)
        return self
    
    def make_deposit_to_savings(self, amount):
        self.savings_account.deposit(amount)
        return self

    def make_withdrawl_from_checking(self, amount):
        self.checking_account.withdraw(amount)
        return self
    
    def make_withdrawl_from_savings(self, amount):
        self.savings_account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"Checking Account: ${self.checking_account.balance}")
        print(f"Savings Account: ${self.savings_account.balance}")
        return self

    def transfer_money_from_checking(self, amount, user):
        self.checking_account.transfer_money(amount, user)
        return self
    
    def transfer_money_from_savings(self, amount, user):
        self.savings_account.transfer_money(amount, user)
        return self



harrison = User("Harrison", "Anthony", "harrisoneanthony@gmail.com", 32)
hayley = User("Hayley", "Finik", "hfinik@nobull.com", 26)
bella = User("Bella", "Alzendez", "bella.@dog.com", 3)


harrison.make_deposit_to_checking(100).make_deposit_to_savings(100).display_user_balance()