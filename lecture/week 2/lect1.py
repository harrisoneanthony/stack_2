import random
import math

# create a funtion that helps my monkey friend ted collect a random amount of bananas between 1 and 50. 
# if the random generated number is even print "you have an even number of bananas" and how many.
# Then return the random value of bananas

# print(math.floor(random.random()*51))

def bananas():
    num_bananas = math.floor(random.random()*51)
    if num_bananas % 2 == 0:
        print(f"Ted you have {num_bananas} bananas, which is even!!")
    else:
        print(f"Sorry Ted, these {num_bananas} bananas are a little odd!!")
bananas()

# Dictionary loops
games = {
    "atari": "asteroids",
    "xbox": "Halo",
    "playstation": "Crash bandit coot",
    "nintendo_64": "goldeneye",
}

# .keys()
print(games.keys())
for key in games.keys():
    print(key)
    print(games[key])

# .values()
for val in games.values():
    print(val)

#  .items()
print(games.items())
    # prints tuples in a list