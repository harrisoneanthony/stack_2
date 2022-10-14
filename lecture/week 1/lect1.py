# print("Hello World!")

# Datatypes
# # Strings
# name = "Harrison"
# dog = "Bella"
# new_name = name + str(10)
# print(name + " has a dog named " + dog)
# print(f"{name} has a dog named {dog}")

#Integers
# luckyt_number = 7

# Floats
# 2.5

# Booleans
# is_instructor = False

# # tuples
# cars = ("BMW", "Nissan", "Honda")
# print(cars[1])

# Lists
# movies = ["back to the future", "batman", "step brothers"]
# print(movies[2])
# movies.append("My cousin Vinny")
# movies.pop(1)
# print(movies)

# Dictionaries
# robot = {
#     "name": "Wall-E",
#     "antenas": 10,
#     "leg_type": "tread",
#     "materials": "steel"
# }

# print(robot["name"])

# conditionals
# indentations
# weather = "foggy"
# if weather == "rainy":
#     print("Bring an umbrella!!!")

# elif weather == "sunny":
#     print("Wear some shorts!!!")

# else:
#     print(f"Prepare for {weather}!!")



#  Building functions
weather = input("what's the weather like?")

def weather_teller(weather):
    if weather == "rainy":
        print("Bring an umbrella!!!")
    elif weather == "sunny":
        print("Wear some shorts!!!")
    else:
        print(f"Prepare for {weather}!!")

weather_teller(input("what's the weather like?")) # then type "rainy", "sunny", or something else in terminal to get that response printed

# for loops
# for i in range(6):
#     print(i)


# games = ["Apex Legends", "Elden Ring", "Dreamlight Valley"]

# i = 0
# while i < len(games):
#     print(games[i])
#     i += 1

# for loop
# while loop
# loop through a string

# weather = "whats the weather?"
# for i in range(len(weather)):
#     print(i)

# for char in weather:
#     print(char)


games = {
    "xbox_one": "apex legends",
    "playstation": "god of war",
    "nes": "duck hunt"
}

print(games["nes"])

for key in games:
    print(games[key])

# loop through multiples of any number
#  building functions