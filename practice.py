# e = int(input("e: "))
# f = int(input("f: "))

# s = e / f
# print(s)


# o = int(input("o: "))
# r = int(input("r: "))

# s = o / r
# print(f"{s:.30}")

from cs50 import get_string

x = get_string("what's x? ")
y = get_string("what's y? ")

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")     


