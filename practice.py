from cs50 import get_string , get_int

answer = get_string("what's your name? ")
print(f"hello , {answer}")

answer = input("what's your number? ")
print(f"hello , {answer}")
          

r = get_int("r: ")
o = get_int("o: ") 

print(r + o)

j = int(input("j: "))
p = int(input("p: "))

print(j + p)

u = int(input("u: "))
y = int(input("y: "))

f = u / y
print(f)

q = int(input("q: "))
l = int(input("l: "))

j = q / l
print(f"{j:.40f}")

x = get_int("what's x? ")
o = get_int("what's y? ")

if (x < o):
    print("x is less than o")

elif (x > o):
    print("x is greater than o")

else:
    print("x and o are equal")

def sort_list():
    print("list has been sorted")


sort_list()

def sort_list():
    while True:
        print("list has been sorted")



sort_list()        

def sort_list():
    for i in range(3):
        print("list has been sorted")


sort_list()        

def sort_list():
    sort_list = 0
    while sort_list < 3:
        sort_list += 1
        print("list has been sorted")


sort_list()

names = ["Jessica" , "Dutch" , "Lily"]
name = get_string("Names: ")

if name in names:
    print("found")

else:
    print("not found")

scores = []
for i in range(3):
    player = get_int("Score: ")
    scores.append(player)

average = sum(scores) / len(scores)
print(f"Average: {average}")    

def system():
    for i in range(3):
        load_file()
     


def load_file():
    print("system is corrupted")


system()

def greet(name):
    print(f"hello, {name}")



greet("Ella")    

