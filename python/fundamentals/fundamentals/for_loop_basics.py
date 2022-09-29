# 1. basics
for i in range(151):
    print(i)

# 2. multiples of 5
for i in range(5,1001,5):
    print(i)

# 3. Counting, the Dojo way
for i in range(101):
    if i%10 == 0:
        print("Coding Dojo")
    elif i%5 == 0:
        print("Coding")
    else:
        print(i)

# 4. Whoa. That Sucker's Huge
numbers = range(0,5000,1)
Sum = sum(numbers)
print(Sum)

# 5. Countdown by 4s
for i in range (2018,0,-4):
    print(i)

# 6. Flexible Counter
low_num = 2
high_num = 9
mult = 3
for i in range(low_num,high_num):
    if i % mult == 0:
        print(i)

