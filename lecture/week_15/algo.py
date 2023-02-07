''' A storeroom is used to organize items stored in it on N shelves. Shelves are numbered from 0 to N-1.
The K-th shelf is dedicated to items of only one type, denoted by a positive integer A[K].

Recently it was decided that it is necessary to free R consecutive shelves. Shelves cannot be reordered. What is
the maximum number of types of items which still can be stored in the storeroom after freeing R consecutive shelves?

Write a function:

    def solution(A,R)
    
that, given an array of A of N integers representing types of items stored on storeroom shelves, and an integer R representing the number of consecutvie shelves to be freed, returns the maximum number of different types of items that can be stored in the storeroom after freeing R consecutive shelves

Examples:

1. Given A = [2,1,2,3,2,2] and R = 3, your function should return 2. It can be achieved, for example by freeing shelves 2,3 and 4 (shelves are numbered from 0)

2. Given A =[2,3,1,1,2] and R = 2, your function should return 3. All three types can still be stored by freeing the last two shelves

3. Given A = [20, 10, 10, 10, 30, 20] and R = 3, your function should return 3. It can be achieved by freeing the first three shelves.

4. Given A = [1, 100000, 1] and R = 3, your function should return 0. All shelves need to be freed.

AKA::: given an array, remove the number (R) of indexies in a row that will return the maximum number of different values'''

def solution(A, R):
    shelf = {}
    for i in range(0, len(A)):
        if A[i] not in shelf:
            shelf[A[i]] = 1
        else:
            shelf[A[i]] += 1

# print(solution([2,1,2,3,2,2], 3)) # == 2
# print(solution([2, 3, 1, 1, 2], 2)) # ==3
# print(solution([20, 10, 10, 10, 30, 20], 3)) # ==3
# print(solution([1, 1000, 1], 3)) # ==0


'''There is a bus moving in the city which takes and drops some people at each bus stop.

You are provided with a list (or array) of integer pairs. Elements of each pair represent the number of people that get on the bus (the first item) and the number of people that get off the bus (the second item) at a bus stop.

Your task is to return the number of people who are still on the bus after the last bus stop (after the last array). Even though it is the last bus stop, the bus might not be empty and some people might still be inside the bus, they are probably sleeping there :D

Take a look on the test cases.

Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the returned integer can't be negative.

The second value in the first pair in the array is 0, since the bus is empty in the first bus stop.

        test.assert_equals(number([[10,0],[3,5],[5,8]]),5)
        test.assert_equals(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]),17)
        test.assert_equals(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]),21)'''


def number(bus_stops):
    return sum([I[0] - I[1] for I in bus_stops])

# print(number([[10,0],[3,5],[5,8]]))
# print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
# print(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]))


'''Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.

For example:

solution([1,2,3,10,5]) # should return [1,2,3,5,10]
solution(None) # should return []'''

def solution(nums):
    return []if nums == None or nums == [] else nums.sort()


# print(solution([1,2,3,10,5]))
# print(solution(None))



'''Skyline Heights
Lovely Burbank has a breathtaking view of the Los Angeles skyline. Let’s say you are given an array with heights of consecutive buildings, starting closest to you and extending away. Array [-1,7,3] would represent three buildings: first is actually out of view below street level, behind it is second at 7 stories high, third is 3 stories high (hidden behind the 7-story). You are situated at street level. Return array containing heights of buildings you can see, in order. Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4]. As always with challenges, do not use built-in array functions such as unshift().'''


def skyline(heights):
    visible = []
    prev_height = -1
    for height in heights:
        if height > prev_height:
            visible.append(height)
        prev_height = height
    return visible

print(skyline([-1,1,1,7,3]))
print(skyline([0,4]))
