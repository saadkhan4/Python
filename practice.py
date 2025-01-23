from cs50 import get_string, get_int

answer = get_string("what's your name? ")
print(f"hello , {answer}")

answer = input("what's your name? ")
print(f"hello , {answer}")

c = get_int("c: ")
f = get_int("f: ")

print(c + f)

g = int(input("g: "))
p = int(input("p: "))

print(g + p)

b = int(input("b: "))
h = int(input("h: "))

print(b - h)

j = int(input("j: "))
l = int(input("l: "))

print(j * l)

k = int(input("k: "))
o = int(input("o: "))

z = k / o
print(z)

c = int(input("c: "))
r = int(input("r: "))

v = c / r
print(f"{v:.56f}")

v = int(input("v: "))
o = int(input("o: "))

if (v > o):
    print("v is greater than o")

elif (v < o):
    print("v is less than o")

else:
    print("v and o are equal")

b = input("b: ")
o = input("o: ")

if b == o:
    print("same")

else:
    print("different")    


def save_data():
    print("data is saved")


save_data()

def save_data():
    print("data is saving")


save_data()


def sys_loop():
    for i in range(3):
        print("data is saving")



sys_loop()


def sys_loop():
    sys_loop = 0
    while sys_loop < 3:
        sys_loop += 1
        print("loop has been started")


sys_loop()


names = ["Ali","Jess","Hamza"]
name = input("Name: ")

if name in names:
    print("found")


else:
    print("not found")


scores = []
for i in range(3):
    player = int(input("Scores: "))
    scores.append(player)

average = sum(scores) / len(scores)
print(f"Average: {average}")


def greet(name):
    print(f"hello ,{name}")

greet("Natasha")    


def system():
    for i in range(3):
        loop()


def loop():
    print("system loop has been initiated")



system()           



def odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
num = int(input("Enter a number: "))
print(f"The number {num} is {odd_or_even(num)}")

def reverse_string(input_string):
    return input_string[::-1]

user_input = input("Enter your string: ")
print(f"The reverse string is {reverse_string(user_input)}")


def unique_number(numbers):
    unique_number = sorted(set(numbers),reverse=True)
    return unique_number[1]


num_list = [12,54,55,44,60,60,2013] 
print(f"The second largest number is {unique_number(num_list)}")