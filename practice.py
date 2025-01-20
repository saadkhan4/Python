from cs50 import get_string, get_int

answer = get_string("what's your name? ")
print(f"hello , {answer}")

reply = input("what's your name? ")
print(f"hello , {reply}")

r = get_int("r: ")
p = get_int("p: ")

print(r + p)

u = int(input("u: "))
p = int(input("p: "))

print(u + p)
 
j = int(input("j: "))
p = int(input("p: "))

print(j - p)

b = int(input("b: "))
k = int(input("k: "))

print(b * k)

m = int(input("m: "))
l = int(input("l: "))

o = m / l
print(o)

s = int(input("s: "))
n = int(input("n: "))

m = s / n 
print(f"{m:.40f}")

u = int(input("u: "))
l = int(input("l: "))

if (u < l):
    print("u is less than l")

elif(u > l):
    print("u is greater than l")

else:
    print("u and l are equal")        

x = input("x: ")
g = input("g: ")

if x == g:
    print("same")

else:
    print("different")

games = ["Resident Evil","Fortnite","Cyberpunk 2077"]
game = input("Game: ")
if game in games:
    print("Found")

else:
    print("Not found")    

scores = []
for i in range(3):
    player = int(input("Score: "))
    scores.append(player)

average = sum(scores) / len(scores)
print(f"Average: {average}")    

def system_loop():
    while True:
     print("loop has been started")


system_loop()    

def system_loop():
    for i in range(3):
        print("loop has been started")


system_loop()        

def system_loop():
    system_loop = 0
    while system_loop < 3:
        system_loop += 1
        print("loop has been started")


system_loop()

def system():
    for i in range(3):
        truncation()



def truncation():
    print("inter has been truncated")


system()    

def greet(name):
    print(f"hello , {name}") 



greet("Natasha")           

def odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
num = int(input("Enter a number: "))
print(f"The number {num} is {odd_or_even(num)}")    

def reverse_string(input_string):
    return input_string[::-1]

user_input = input("Enter a string: ")
print(f"The reverse string is {reverse_string(user_input)}")
