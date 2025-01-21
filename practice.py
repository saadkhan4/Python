from cs50 import get_string, get_int

answer = get_string("what's your name? ")
print(f"hello , {answer}")

answer = input("what's your name? ")
print(f"hello , {answer}")

c = get_int("c: ")
o = get_int("o: ")

print (c + o)

b = int(input("b: "))
m = int(input("m: "))

print(b + m)

n = int(input("n: "))
l = int(input("l: "))

print(n - l)

r = int(input("r: "))
p = int(input("p: "))

print(r * p)

x = int(input("x: "))
i = int(input("i: "))

f = x / i
print(f)

u = int(input("u: "))
q = int(input("q: "))

h = u / q
print(f"{h:.50f}")

n = int(input("n: "))
o = int(input("o: "))

if (n < o):
    print("n is less than o")

elif (n > o):
    print("n is greater than o")

else:
    print("n and o are equal")

def break_loop():
    print("loop ends here")


break_loop()


def break_loop():
    while True:
        print("loop ends here")


break_loop()


def break_loop():
    for i in range(3):
        print("loop ends here")


break_loop()



def system_loop():
    system_loop = 0
    while system_loop < 3:
        system_loop += 1
        print("loop ends here")


system_loop()        


v = input("v: ")
p = input("p: ")

if v == p:
    print("same")

else:
    print("different")

names = ["Jade", "Julia","Jess"] 
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


def system():
    for i in range(3):
        system_loop()



def system_loop():
    print("loop initiate from here")        


system()    

def greet(name):
    print(f"hello ,{name}")


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

input_string = input("Enter a string: ")
print(f"The reverse string is {reverse_string(input_string)}")


def second_largest(numbers):
    unique_number = sorted(set(numbers), reverse=True)
    return unique_number[1]

num_list = [10 , 120 , 555 , 144 , 56, 56]
print(f"The second largest number is {second_largest(num_list)}")

    