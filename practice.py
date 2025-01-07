from cs50 import get_int, get_string

answer = get_string("what's your name? ")
print(f"hello , {answer}")

answer = input("what's your name? ")
print(f"hello , {answer}")

p = get_int("p: ")
o = get_int("o: ")

print(o + p)

l = int(input("l: "))
p = int(input("p: "))

print(l + p)

j = int(input("j: "))
b = int(input("b: "))

p = j / b
print(p)

k = int(input("k: "))
p = int(input("p: "))

l = k / p
print(f"{l:.40f}")

def position():
    print("Fixed position")


position()    

def position():
    for position in range(3):
        print("Fixed position")


position()        

def position():
    position = 0
    while position < 3:
        position += 1 
        print("Fixed position")


position()

scores = []
for i in range(3):
    player = get_int("Score: ")
    scores.append(player)

average = sum(scores) / len(scores)
print(f"Average: {average}")  


names = {"Ali","Sara" ,"Hamza"}
name = get_string("Names: ")

if name in names:
    print("Found")

else:
    print("Not Found")    

def system():
    for i in range(3):
        obstruction()


def obstruction():
    print("System Repeated")        


system()    
    
def greet(name):
    print(f"hello ,{name}")


greet("Natasha")   