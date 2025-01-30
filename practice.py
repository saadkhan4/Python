from cs50 import get_string , get_int

answer = get_string("what's your name? ")
print(f"hello, {answer}")

answer = input("what's your name? ")
print(f"hello ,{answer}")

r = get_int("r: ")
o = get_int("o: ")

print (r + o)

b = int(input("b: "))
q = int(input("q: "))

print(b - q)

v = int(input("v: "))
t = int(input("t: "))

print(v * t)

h = int(input("h: "))
m = int(input("m: "))

c = h / m
print(c)

p = int(input("p: "))
z = int(input("z: "))

c = p / z
print("{c:.40f}")

b = int(input("b: "))
n = int(input("n: "))

if (b < n):
    print("b is less than n")

elif (b > n):
    print("b is greater than n")

else:
    print("b and n are equal") 


v = input("v: ")
l = input("l: ")

if v == t:
    print("same")

else:
    print("different")


names = ["Ali","Jesse","Rose"]
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
    print("format system")


system()


def system():
    while True:
        print("format system")


system()


def formate_date():
    for i in range(3):
        print("date has been formatted")


formate_date()


def system():
    system = 0
    while system < 3:
        system += 1
        print("system is corrupted")


system()    


def sys_loop():
    for i in range(3):
        system()


def system():
    print("access to system")


sys_loop()



def greet(name):
    print(f"hello {name}")


greet("Natasha")


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
num = int(input("Enter your number: "))
print(f"The number {num} is {even_or_odd(num)}")   


def reverse_string(input_string):
    return input_string [::-1]

user_input = input("Enter your string: ")
print(f"The reverse string is {reverse_string(user_input)}")

def unique_number(numbers):
    unique_number = sorted(set(numbers),reverse=True)
    return unique_number[1]

num_list = [32,43,12,22,44,1233]
print(f"The second largest number is {unique_number(num_list)}")












