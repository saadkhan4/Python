from cs50 import get_string, get_int

answer = get_string("what's your name? ")
print(f"hello , {answer}")

reply = get_string("what's your name? ")
print(f"hello , {reply}")

f = get_int("f: ")
j = get_int("j: ")

print(f + j)

h = int(input("h: "))
p = int(input("p: "))

print(h + p)

g = int(input("g: "))
e = int(input("e: "))

q = g / e
print(q)

q = int(input("q: "))
o = int(input("o: "))

b = q / o
print(f"{b:.43f}")

j = int(input("j: "))
p = int(input("p: "))

print(j * p)

i = int(input("i: "))
l = int(input("l: "))

print(i - l)

u = int(input("u: "))
o = int(input("o: "))

if (u < o):
    print("u is greater than o")

elif (u > o):
    print("u is less than o")

else:
    print("u and o are equal")        

def end_game():
    print("game has been ended")


end_game()    

def end_game():
    while True:
        print("game has been ended")


end_game()

def system_loop():
    for i in range(3):
        print("loop will begin")


system_loop()       

def system_loop():
    system_loop = 0
    while system_loop < 3:
        system_loop += 1
        print("loop will begin")


system_loop()        

names = ["Jess","Coop","Charlotte"]
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

def main():
    for i in range(3):
        system()



def system():
    print("System is malfunctioning")


main()           

def greet(name):
    print(f"hello ,{name}")


greet("name")    

d = input("d: ")
r = input("r: ")

if d == r:
    print("same")


elif d != r:
    print("different") 