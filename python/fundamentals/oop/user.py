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
        if self.gold_card_points > amount:
            self.gold_card_points -= amount
        else:
            print("insufficent funds")


harrison = User("Harrison", "Anthony", "harrisoneanthony@gmail.com", 32, True, 100)
hayley = User("Hayley", "Finik", "hfinik@nobull.com", 26, False, 0)
bella = User("Bella", "Alzendez", "bella.@dogcom", 3, False, 0)

harrison.spend_points(50)
harrison.display_info()

hayley.enroll()
hayley.spend_points(80)
hayley.display_info()

harrison.display_info()
hayley.display_info()
bella.display_info()

harrison.enroll()
bella.spend_points(10)