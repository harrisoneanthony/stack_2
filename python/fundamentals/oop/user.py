from operator import truediv


class User:		
    def __init__(self, first_name, last_name, e_mail, age, is_rewards_member, gold_card_points):
        self.first_name = first_name
        self.last_name = last_name
        self.e_mail = e_mail
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.e_mail)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
    
    def enroll(self):
        if self.is_rewards_member == True:
            print("user is already a member")
            return True
        else:
            self.is_rewards_member = True
            self.gold_card_points += 200
            return False

    def spend_points(self, amount):
        self.gold_card_points -= amount

harrison = User("Harrison", "Anthony", "harrisoneanthony@gmail.com", 32, False, 0)

# display_info(self) - Have this method print all of the users' details on separate lines.
harrison.display_info()

# enroll(self) - Have this method change the user's member status to True and 
#     set their gold card points to 200.
harrison.enroll()
harrison.display_info()

# spend_points(self, amount) - have this method decrease the user's points by 
#     the amount specified.
harrison.spend_points(100)
harrison.display_info()

# Ninja Bonuses:

# Add logic in the enroll method to check if they are a member already, and if 
# they are, print "User already a member." and return False, otherwise return True.

harrison.enroll()

# Add logic in the spend points method to be sure they have enough points to spend 
# that amount and handle appropriately.


