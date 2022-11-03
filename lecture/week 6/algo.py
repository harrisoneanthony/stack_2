'''create a function that given a string, returns the intger made from the strings
digits. Given 0s1a3y5wh9a2t4 the function should return 01357924'''


def intergers(input):
    digits = ''
    for char in input:
        print(char)
        if char.isalpha():
            continue
        else:
            digits += char
    return digits
print(intergers('0s1a3y5w7h9a2t4'))