'''create a function that returns whether the second string is a permutation of the first. for example, given ("mister", "stimer") return true. Given ("mister", "sister"), return false'''

# create a function
# for loop to iterate through strings
#  if statement

def second_string(input1,input2):
    permutation = ''
    for char in input1:
        for char2 in input2:
            if char == char2:
                permutation += char
                break
    if permutation == input1:
        return True
    return False

print(second_string("mister", "stimer"))
print(second_string("mister", "sister"))