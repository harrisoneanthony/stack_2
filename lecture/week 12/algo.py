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

# print(count_character('aaababbacddd'))
# print(count_character('HeLlo'))
# print(count_character({}))


def count_character(s):
    return {i: s.count(i) for i in s}
            

# print(count_character('aaababbacddd'))
# print(count_character('HeLlo'))
# print(count_character({}))



# write the function is_anagram
def is_anagram(test, original):
# get lower case of test, original
    lower_test = test.lower()
    lower_original = original.lower()
# add characters and count to dictionaries
    test_dict = {i: lower_test.count(i) for i in lower_test}
    original_dict = {i: lower_original.count(i) for i in lower_original}
# compare dictionaries
# if dictionary 1 == dictionary 2 true else false
    print(test_dict, original_dict)
    if test_dict == original_dict:
        return True
    else:
        return False

# print(is_anagram("foefet", "toffee")) #true
# print(is_anagram("Buckethead", "DeathCubeK")) #true
# print(is_anagram("Twoo", "WooT")) #true
# print(is_anagram("dumble", "bumble")) #false
# print(is_anagram("ound", "round")) #false
# print(is_anagram("apple", "pale")) #false
# print(is_anagram("aa", 'a'))



'''Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
Write a function which takes a list of strings and returns each line prepended by the correct number.
The numbering starts at 1. The format is n: string. Notice the colon and space in between.
Examples: (Input --> Output)

[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]'''

def number(lines):
    x = 1
    for i in range(len(lines)):
        lines[i] = str(x) + ": " + lines[i]
        x+=1
    return lines
# print(number(['a', 'b', 'c']))

