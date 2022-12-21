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

print(is_palindrome('Atoyota'))

