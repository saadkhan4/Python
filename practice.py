from cs50 import get_string , get_int

answer = input("what's your name? ")
print(f"hello ,{answer}")

answer = get_string("what's your name? ")
print(f"hello ,{answer}")

v = get_int("v: ")
t = get_int("t: ")

print(v + t)

c = int(input("c: "))
p = int(input("p: "))

print(c - p)

x = int(input("x: "))
q = int(input("q: "))

print(x * q)


r = int(input("r: "))
w = int(input("w: "))

print(r / w)

q = int(input("q: "))
k = int(input("k: "))

r = q / k
print(r)


d = int(input("d: "))
l = int(input("l: "))

g = d / l
print(f"{g:.43f}")

x = int(input("x: "))
s = int(input("s: "))

if (x < s):
    print("x is less than s")

elif(x > s):
    print("x is greater than s")

else:
    print("x and s are equal")


f = input("f: ")
d = input("d: ")


if (f == d):
    print("same")


else:
    print("different")


names = ["Ali","Jess","Cassandra"]
name = input("Name: ")

if name in names:
    print("found")

else:
    print("not found")


scores = []
for i in range(3):
    player = int(input("Score: "))
    scores.append(player)

average = sum(scores) / len(scores)
print(f"Average: {average}")


def system():
    print("system is running")


system()



def sys_loop():
    for i in range(3):
        print("system loop started from here")


sys_loop()


def sys_loop():
    while True:
        print("loop begins from here")


sys_loop()


def sort_array():
    sort_array = 0
    while sort_array < 3:
        sort_array += 1
        print("array has been solved")


sort_array()


def greet(name):
    print(f"hello,{name}")


greet("Natasha")

def main():
    for i in range(3):
        system_loop()



def system_loop():
    print("loop started from here")



main()


def odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

num = int(input("Enter your number: "))
print(f"The number {num} is {odd_or_even(num)}")


def reverse_string(input_string):
    return input_string [::-1]

user_input = input("Enter your string: ")
print(f"The reverse string is {reverse_string(user_input)}")


def second_largest(numbers):
    unique_number = sorted(set(numbers),reverse=True)
    return unique_number[1]


num_list = [32,42,2,4,5412,343,12]
print(f"The second largest number is {second_largest(num_list)}")













