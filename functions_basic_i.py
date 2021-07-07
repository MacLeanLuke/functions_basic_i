#1
# def number_of_food_groups():
#     return 5
# print(number_of_food_groups())
# # will print the number 5


# #2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# # will return an name error because the function number_of_days_in_a_week_silicon_or_triangle_sides() is undefined


# #3
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())
# # will return the value 5 because it is the first return statement that is valid


# #4
# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())
# # will return the value 5 and will not print 10 to the console because the return function acts like a break, and kills any other process that comes after it.


# #5
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes()
# print(x)
# # will see 4 printed to the terminal, however no value is passed from the function itself. the only reason something is printed the the terminal is because the function explicity calls for the process.
# # Interesting after runnning the process, I now see that when the print function is called on the variable, it prints none to the console, because that is was was returned from the function. 


# #6
# def add(b,c):
#     print(b+c)
# print(add(1,2) is add(2,3))
# # this will print 3 and 5 to the console as called in the function, however when the print statement is called outside of the function, I believe it will return something like None or None None or 0. I'm not sure how None is handled in a mathmatic expression.
# # In fact, when I ran this it returned, an error because the None-type does not take the operand +. However we could use the word "is" which should return true.
# # that was correct!


# #7
# def concatenate(b,c):
#     return str(b)+str(c)
# print(concatenate(2,5))
# # this will return "25" because the function will stringify the integers and concatenate them on the return statement


# #8
# def number_of_oceans_or_fingers_or_continents():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(number_of_oceans_or_fingers_or_continents())
# # This function does not take any parameters, so it is simply run when called. First the function sends a print statement to the console of the value assigned the varaible b which is 100; then an if statement evaluates b against the value 10, which is greater than. So, if defaults to the else statement which triggers a return statement passing the integer 10 from the function and killing any other processes after it. Finally, the print function prints the returned  value 10 from the function to the console


# #9
# def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# # first of all, why does this function have such a long name? This will run through the function 4 times each time evaluating b is less than c. if b is less than c than the function will return 7, however if b is less than c evaluates to false, the function returns 14. at no point will this function ever return 3. the console will print 7 14 and 21 for the last print call because the return statements are added together.


# #10
# def addition(b,c):
#     return b+c
#     return 10
# print(addition(3,5))
# # this function will return the value of b and c added together every time. under no circumstances will this return 10. the value 8 will be printed to the console.


# #11
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
# print(b)
# foobar()
# print(b)
# # this will print the variable b as defined outside of the function 3 times, however when the function is called and the the function prints b as defined by the function it will do so. the console will read 500 500 300 500


# # #12
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# foobar()
# print(b)
# # this will do something similar to the one before. but the function will first prin the value of b to the console and then return it, however there isn't a print statement from result of the function, so no biggie. the console will read 500 500 300 500


# #13
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=foobar()
# print(b)
# # this time the the variable b is set to the value of the return value from the funtion foobar. the console will read. 500 500 300 300


# #14
# def foo():
#     print(1)
#     bar()
#     print(2)
# def bar():
#     print(3)
# foo()
# # this in is an interesting one. when foo is called it first prints teh value 1 to the console and then it in turn calls the function bar which prints 3 and then foo finally prints 2


# #15
# def foo():
#     print(1)
#     x = bar()
#     print(x)
#     return 10
# def bar():
#     print(3)
#     return 5
# y = foo()
# print(y)
# # console log 1 3 5 10 