from cs50 import get_int
# # with the help of cs50 library

# x = get_int("x: ")
# y = get_int("y: ")

# print(x + y)

# without help of cs50 library we use int & input so the integers can behave as int..

# s = int(input("s: "))
# t = int(input("t: "))

# print(s + t)

#  TRUNCATION #

# x = int(input("x: "))
# y = int(input("y: "))

# z = x / y
# print(z) # this is how you truncate the value in python #

# FLOATING POINT IMPRECISION #

r = int(input("r: "))
s = int(input("s: "))

z = r / s 
print(f"{z:.50f}")   # after this you can see other integers after the decimal.


