def narcissist(num):
    len_of_num = len(str(num))
    result = 0
    for char in str(num):
        result += int(char)**int(len_of_num)
    if result == num:
        return True

# print(narcissist(153))

def narcissist(num):
    return num == sum([int(x) ** len(str(num)) for x in str(num)])

# print(narcissist(153))


# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
    new_str =""
    count = 0
    cap_str = s.upper()
    for i in cap_str:
        new_str += i
        if count > 0:
            new_str +=i.lower()*count
        count += 1
        if count < len(s):
            new_str += '-'
    return new_str
        

# print(accum("ZpglnRxqenU"))
# print(accum("NyffsGeyylB"))
# print(accum("MjtkuBovqrU"))
# print(accum("EvidjUnokmM"))
# print(accum("HbideVbxncC"))

'''Given a list of integers return a new list moving all of the zeros to the back of the list
example: [ 0, 2, 1, 6, 4, 3, 6, 0, 3 ] would return [2, 1, 6, 4, 3, 6, 3, 0, 0]'''

def move_zeros(l):
    for i in l:
        if i == 0:
            l.remove(i)
            l.insert(len(l),i)
    return l

print(move_zeros([0, 2, 1, 6, 4, 3, 6, 0, 3]))