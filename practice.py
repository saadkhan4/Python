from cs50 import get_string , get_int

answer = get_string("What's your name? ")
print(f"hello , {answer}")

answer = input("what's your name? ")
print(f"hello , {answer}")

f = get_int("f: ")
t = get_int("t: ")

print(f + t)

g = int(input("g: "))
l = int(input("l: "))

print(g + l)

b = int(input("b: "))
m = int(input("m: "))

print(b - m)

v = int(input("v: "))
o = int(input("o: "))

print(v * o)

c = int(input("c: "))
k = int(input("k: "))

l = c / k
print(l)

s = int(input("s: "))
a = int(input("a: "))

m = s / a 
print(f"{m:.40f}")

b = int(input("b: "))
u = int(input("u: "))

if (b < u):
    print("b is less than u")

elif (b > u):
    print("b is greater than u")

else:
    print("b and u are equal")


d = input("d: ")
b = input("b: ")

if d == b:
    print("same")

else:
    print("different") 



names = ["Ali", "Sam","Hamza"]
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



def formate_date():
    print("date has been formatted")


formate_date()


def system_loop():
    while True:
        print("loop has been started")

system_loop()



def system_loop():
    for i in range(3):
        print("loop has been started")


system_loop()


def download_file():
    download_file = 0
    while download_file < 4:
        download_file += 1
        print("file will download soon")


download_file()


def greet(name):
    print(f"hello , {name}")



greet("Natasha")



def system():
    for i in range(3):
        loop()



def loop():
    print("loop has been initiated")




system()



def odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

num = int(input("Enter a number: "))
print(f"The number {num} is {odd_or_even(num)}")    


def reverse_string(input_string):
    return input_string [::-1]

user_input = input("Enter a string: ")
print(f"The reverse string is {reverse_string(user_input)}")



def unique_number(numbers):
    unique_number = sorted(set(numbers), reverse=True)
    return unique_number[1]


num_list = [12,44,23,332,33,23,12]
print(f"The second largest number is {unique_number(num_list)}")