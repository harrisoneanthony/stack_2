# String: is palindrome
# Create a function that return s aboolean wheter the string is a strict palindrom
# palindrome = string that is same forwards and backwards
# ex. atoyota
# do not ignore spaces, punctuation and capitalization

def is_palindrome(str):
    if (str == str[::-1]):
        return True
    else:
        return False
    

def is_palindrome(string):
    count = len(string)-1
    # create a loop to go through each char of str
    for char in string:
        if char != string[count]:
            return False
        count -= 1
    return True

# print(is_palindrome('Atoyota'))


'''The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

ex 2: "aaababbacddd" --> {'a':5, 'b': 3, 'c':1,'d':3}
ex 3: "Hello" --> {'h': 1,'e':1, 'l': 2, 'o':1}

What if the string is empty? Then the result should be empty object literal, {}.
**Make sure every key in your dictionary is lowercase.''' 

def count_character(s):
    # create an empty dictionary
    counts = {}
    # iterate through each character in the string
    for c in s:
        # convert the character to lowercase
        c = c.lower()
        # if the character is not in the dictionary, add it with a count of 1
        if c not in counts:
            counts[c] = 1
        #  if the character is already in the dictionary, inrement the count by 1
        else:
            counts[c] += 1
    return counts

print(count_character('aaababbacddd'))
print(count_character('HeLlo'))
print(count_character({}))


def count_character(s):
    return {i: s.count(i) for i in s}
            

print(count_character('aaababbacddd'))
print(count_character('HeLlo'))
print(count_character({}))
