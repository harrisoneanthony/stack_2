'''implement the function which takes an array containing the names of people that like
an item. It must return the display text as shown in the examples

[]                                --> "no one likes this"
["Peter"]                         --> "Peter likes this"
["Jacob", "Alex"]                 --> "Jacob and Alex like this"
["Max", "John", "Mark"]           --> "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  --> "Alex, Jacob, and 2 others like this"'''


def likes(names):
    if len(names) == 0:
        return "no one likes"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]}, {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]}, {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names)-2} others like this"



print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Alex", "Jacob", "Mark", "Max"]))



'''Sum to one Digit
Implement a function sumToOne(num) that, given a number, sums that numbers digits
repeatedly until the sum is only on digit. Return that final lone digit result.
5789 -> 5+7+8+9 = 29
29 -> 2+9 = 11
11 -> 1+1 = 2'''

