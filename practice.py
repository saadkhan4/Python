from cs50 import get_string, get_int

answer = get_string("what's your name? ")
print(f"hello , {answer}")

answer = input("what's your age? ")
print(f"I'm {answer}")

r = get_int("r: ")
k = get_int("k: ")

print(r + k)

e = int(input("e: "))
h = int(input("h: "))

print(e * h)

g = int(input("g: "))
o = int(input("o: "))

f = g / o
print(f)

k = int(input("k: "))
p = int(input("p: "))

d = k / p
print(f"{d:.40f}")

g = int(input("g: "))
d = int(input("d: "))

print(g - d)

g = get_int("what's g? ")
u = get_int("what's u? ")

if (g < u):
    print("g is less than u")

elif (g > u):
    print("g is greater than u")

else:
    print("g and u are equal")        

def sort_array():
    print("Array has been sorted")

sort_array()    

def sort_array():
    while True:
        print("Array has been sorted")


sort_array()        

def on_button_click():
    for i in range(3):
        print("to this when clicked")


on_button_click()        


def on_button_click():
    on_button_click = 0
    while on_button_click < 3:
        on_button_click += 1
        print("to this when clicked")


on_button_click()


names = ["Jess","Jennifer","Jen"]
name = get_string("Name: ")

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

def main():
    for i in range(3):
        system()



def system():
    print("system is malfunctioning") 


main()           

def greet(name):
    print(f"hello {name}")

greet("Jennifer")    