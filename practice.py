from cs50 import get_int, get_string

x = get_int("x: ")
y = get_int("y: ")

print(x + y)


r = int(input("r: "))
s = int(input("s: "))

print(r + s)


t = int(input("t: "))
y = int(input("y: "))

z = (t / y)
print(z)


y = int(input("y: "))
u = int(input("u: "))

p = y / u
print(f"{p:.80f}")

s = get_string("what's s? ")
e = get_string("what's e? ")

if s < e:
    print("s is less than e")
elif s > e:
    print("s is greater than e")
else:
    print("s is equal to e")

answer = get_string("what's your name? ")
print(f"hello , {answer}")