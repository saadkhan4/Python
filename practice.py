from cs50 import get_int, get_string

answer = get_string("what's your name? ")
print(f"hello ,{answer}")

answer = input("what's your name? ")
print(f"hello , {answer}")

o = get_int("o: ")
p = get_int("p: ")

print(o + p)

i = int(input("i: "))
p = int(input("p: "))

print(i + p)

u = int(input("u: "))
l = int(input("l: "))

print(u - l)

t = int(input("t: "))
s = int(input("s: "))

f = t / s 
print(f)

y = int(input("y: "))
p = int(input("p: "))

g = y / p 
print(f"{g:.50f}")

r = int(input("r: "))
h = int(input("h: "))

print(r * h)

def formate_date():
    print(f"formatting the current date")


formate_date()    

def formate_date():
    while True:
        print(f"formatting the current date")

formate_date()        

def formate_date():
    for i in range(3):
        print(f"formatting the current date")


formate_date()        

def formate_date():
    formate_date = 0
    while formate_date < 3:
        formate_date += 1
        print(f"formatting the current date")

formate_date()        

names = ["Jess","Charlie","Ali"]
name = get_string("Names: ")
if name in names:
    print("found")

else:
    print("not found")    

scores = []
for i in range(3):
    player = get_int("Scores: ")
    scores.append(player)

average = sum(scores) / len(scores) 
print(f"Average: {average}")    

def system():
    for i in range(3):
        sort_array()


def sort_array():
    print(f"array has been sorted")


system()


def greet(name):
    print(f"hello,{name}")



greet("name")

v = int(input("v: "))
p = int(input("p: "))

if (v < p):
    print("v is less than p")

elif (v > p):
    print("v is greater than p")

else:
    print("v and p are equal")    


s = input("s: ")
p = input("p: ")

if s == p:
    print("equal")

elif s != p:
    print("Not equal") 

else:
    print("s and p are equal")       