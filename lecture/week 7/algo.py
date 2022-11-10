'''create a function that, given an input string, returns a booleanwhether
parentheses in that string are valid. Given input "y(3(p)p(3)r)s", return true.
Given "n(0(p)3", return false. Given "n)0(t(0)k", return false'''


# create 2 var
#  a var for boolean to keep track of open and close
# if
# for loop



def input_string(input):
    parentheses = True
    for i in input:
        if i == "(":
            parentheses = True
        elif i == ")":
            parentheses = False
    if parentheses:
        return True
    else:
        return False


print(input_string("y(3(p)p(3)r)s"))
print(input_string("n)0(t(0)k"))