# from cs50 import get_int

# x = get_int("x: ")
# y = get_int("y: ")

# print(x + y)

# with the help of cs50 library

# s = int(input("s: "))
# t = int(input("t: "))

# print(s + t)

# without help of cs50 library we use int & input so the integers can behave as int..

#  TRUNCATION #

# x = int(input("x: "))
# y = int(input("y: "))

# z = x / y
# print(z) # this is how you truncate the value in python #

# FLOATING POINT IMPRECISION #

x = int(input("x: "))
y = int(input("y: "))

z = x / y 
print(f"{z:.50f}")   # after this you can see other integers after the decimal.

 

