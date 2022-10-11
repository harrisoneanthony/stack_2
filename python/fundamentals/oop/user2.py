class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
    
    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()

harrison = User("Harrison")
hayley = User("Hayley")
bella = User("Bella")

harrison.make_deposit(100)
harrison.make_deposit(200)
harrison.make_deposit(50)
harrison.make_withdrawl(45)
harrison.display_user_balance()

hayley.make_deposit(1000)
hayley.make_deposit(1000)
hayley.make_withdrawl(1500)
hayley.display_user_balance()

bella.make_deposit(1000)
bella.make_withdrawl(1500)
bella.make_withdrawl(1500)
bella.display_user_balance()


harrison.transfer_money(300, bella)