class User:
    def __init__(self,data):
        self.first_name = data['fname']
        self.last_name = data['lname']
        self.email = data['email']
        self.password = data['password']

    def update_email(self, new_email):
        self.email = new_email

tony = {
    "fname" : "Tony",
    "lname" : "Hawk",
    "email" : "hawk@hawk.com",
    "password" : "12345678910"
}

fred = {
    "fname" : "Fred",
    "lname" : "Flinstone",
    "email" : "stone@stonge.com",
    "password" : "12345678910"
}

user_tony = User(tony)
user_fred = User(fred)

print(user_fred.email)
user_fred.update_email("wilma@wilma.com")
print(user_fred.email)