'''Write a function:
def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
Write an efficient algorithm for the following assumptions:
•	N is an integer within the range [1..100,000];
•	each element of array A is an integer within the range [−1,000,000..1,000,000].'''

# def solution(A):
#     pos_count = 0
#     for i in A:
#         if i > 0:
#             pos_count += 1
#     if pos_count in A:
#         pos_count -= 1
#     return pos_count


def solution(A):  # Our original array
    m = max(A)  # Storing maximum value
    if m < 1:
        # In case all values in our array are negative
        return 1
    if len(A) == 1:
        # If it contains only one element
        return 2 if A[0] == 1 else 1
    l = [0] * m
    for i in range(len(A)):
        if A[i] > 0:
            if l[A[i] - 1] != 1:
                # Changing the value status at the index of our list
                l[A[i] - 1] = 1
    for i in range(len(l)):
        # Encountering first 0, i.e, the element with least value
        if l[i] == 0:
            return i + 1
            # In case all values are filled between 1 and m
    return i + 2

print(solution([1,3,6,4,1,2]))
print(solution([1,2,3]))
print(solution([-1,-3]))

