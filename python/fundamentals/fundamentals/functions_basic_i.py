# #1 returns 5
# def number_of_food_groups():
#     return 5
# print(number_of_food_groups())



# #2 number_of_days... is not defined
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())


# #3 first return statement ends function. returns 5
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())


# #4 return ends function. returns 5
# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())


# #5 prints 5. x is assigned outside of first function. so 5 then none
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes()
# print(x)


# #6 gets 3 from add(1,2) and 5 from add(2,3) and error from last line. cannot add NoneTypes together
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))


# #7 adds string 2 and string 5 equalling 25
# def concatenate(b,c):
#     return str(b)+str(c)
# print(concatenate(2,5))


# #8 prints 100. Then, since 100 is greater than 10, prints 10. 
# Never hits return 7 because function ends with either return 5 or return 10
# def number_of_oceans_or_fingers_or_continents():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(number_of_oceans_or_fingers_or_continents())


# #9 never returns 3. Returns 7 then 14 then 21
# def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


# #10 doesnt hit return 10. returns 8
# def addition(b,c):
#     return b+c
#     return 10
# print(addition(3,5))


# #11 500,500,300,500. foobar prints 300 but doesn't run until its called on like 86.
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
# print(b)
# foobar()
# print(b)


# #12 500,500,300,500
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# foobar()
# print(b)


# #13 500,500 300, 300. resets b to 300 after function is called so print b prints 300 instead of 500 on last line
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=foobar()
# print(b)


# #14 defines foo(), then defines bar(). prints foo which is 1, bar(),2 or 1,3,2
# def foo():
#     print(1)
#     bar()
#     print(2)
# def bar():
#     print(3)
# foo()


# #15 1,3,5,10
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)