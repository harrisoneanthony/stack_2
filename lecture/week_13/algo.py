'''Create a function that takes in a string input, search through each letter in the string input to find "h", "e", "l" and "p" which spells out help in that order. Return True if found and false if not.

ex: "The last person was Ironman" --> True
ex: "How about them pelicans" --> False
'''

def helpfinder(str):
    new_arr = []
    counth = 0
    counte = 0
    countl = 0
    countp = 0
    for i in str:
        if i == "h":
            while counth == 0:
                counth +=1
                new_arr.append(i)
        if i == "e":
            while counte == 0:
                counte += 1
                new_arr.append(i)
        if i == "l":
            while countl == 0:
                countl += 1
                new_arr.append(i)
        if i == "p":
            while countp == 0:
                countp += 1
                new_arr.append(i)
    if new_arr == ['h','e','l','p']:
        return True
    else:
        return False

print(helpfinder("The last person was Ironman"))
print(helpfinder("How about them pelicans"))