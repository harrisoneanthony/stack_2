import decimal

class BankAccount:

    balance = 0

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


harrison = BankAccount()
hayley = BankAccount()


harrison.display_account_info().deposit(100).display_account_info().deposit(50).display_account_info().deposit(200).display_account_info().withdraw(300).display_account_info()

hayley.display_account_info().deposit(10).display_account_info().deposit(17).display_account_info().withdraw(7).display_account_info().withdraw(1).display_account_info().withdraw(5).display_account_info().withdraw(1).display_account_info().yield_interest().display_account_info()