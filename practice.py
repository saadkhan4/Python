from cs50 import get_string , get_int

answer = get_string("what's your name? ")
print(f"hello ,{answer}")

answer = input("what's your name? ")
print(f"hello ,{answer}")

c = get_int("c: ")
p = get_int("p: ")

print(c + p)

v = int(input("v: "))
k = int(input("k: "))

print(v - k)

t = int(input("t: "))
o = int(input("o: "))

b = t / o
print(b)

q = int(input("q: "))
i = int(input("i: "))

print(q * i)

y = int(input("y: "))
p = int(input("p: "))

g = y / p
print(f"{g:.43f}")

l = int(input("l: "))
u = int(input("u: "))

if (l < u):
    print("l is less than u")

elif(l > u):
    print("l is greater than u")

else:
    print("l and u are equal")    


f = input("f: ")
l = input("l: ")

if (f == l):
    print("same")

else:
    print("different")

names = ["Megan","Dusty","Charlotte"]
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
    print("system is working")


system()

def sys_loop():
    while True:
        print("loop begins from here")

sys_loop()

def machine():
    for i in range(3):
        print("machine is malfunctioning")

machine()


def sys_loop():
    sys_loop = 0
    while sys_loop < 3:
        sys_loop += 1 
        print("loop begins from here")

sys_loop()        

def greet(name):
    print(f"hello , {name}")

greet("Natasha")    

def get_sys_info():
    for i in range(3):
        machine()


def machine():
    print("info is confidential")


get_sys_info()

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
num = int(input("Enter your number: "))
print(f"The number {num} is {even_or_odd(num)}")    

def reverse_string(input_string):
    return input_string[::-1]

user_input = input("Enter your string: ")
print(f"The reverse string is {reverse_string(user_input)}")

def second_largest(numbers):
    unique_number = sorted(set(numbers),reverse=True)
    return unique_number[1]

num_list = [1,4,6,5,23,7,3,98,56,1,3,7,3]
print(f"The second largest number is {second_largest(num_list)}")


def find_duplicates(numbers):
    duplicates = []
    seen = set()

    for num in numbers:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        seen.add(num)


    return duplicates

num_list =  [1,4,6,5,23,7,3,98,56,1,3,7,3]
print(f"The duplicate numbers are {find_duplicates(num_list)}")

def are_anagrams(str1,str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()


    return sorted(str1) == sorted(str2)

print(are_anagrams("Listen", "Silent"))
print(are_anagrams("Hello", "World"))





