from cs50 import get_string, get_int

answer = get_string("what's your name? ")
print(f"hello , {answer}")

answer = input("what's your name? ")
print(f"hello , {answer}")

x = get_int("x: ")
t = get_int("t: ")

print(x + t)

e = int(input("e: "))
p = int(input("p: "))

print(e + p)

d = int(input("d: "))
p = int(input("p: "))

y = d / p
print(y)

o = int(input("o: "))
l = int(input("l: "))

t = o / l
print(f"{t:.50f}")

def obstruction():
    print("Access Denied")


obstruction()    

def obstruction():
    for obstruction in range(5):
        print("Access Denied")


obstruction()        

def obstruction():
    obstruction = 0
    while obstruction < 5:
        obstruction += 1
        print("Access Denied")



obstruction()        


scores = []
for i in range(3):
    player = get_int("Scores: ")
    scores.append(player)

average = sum(scores) / len(scores)
print(f"Average: {average}")    

names = ["Marshall" , "Tobey" , "Jessica"]

name = input("Name: ")
if name in names:
    print("found")

else:
    print("not found")    

def main():
    for i in range(3):
        system()


def system():
    print("System malfunctioning")        



main()    


def greet(name):
    print(f"Hello , {name}")


greet("Jessica")    

