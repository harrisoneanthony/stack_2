''' sum to one digit
implement a function sumToOne(num) that, given a number , sums that number's digits
repeatedly until the sum is only one digit. Return thatfinalonedigitresult
5789 -> 5+7+8+9 =29
29 -> 2+9 = 11
11 -> 1+1 = 2'''

def sum_to_one(num):
    result = num
    num_string = str(num)
    while result > 10:
        for i in range(len(num_string)):
            num_num = int(num_string[i])
            result += num_num
    return result


print(sum_to_one(5789))