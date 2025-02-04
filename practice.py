from cs50 import get_string , get_int

answer = get_string("what's your age? ")
print(f"I'm {answer} years old")

answer = input("what's your name? ")
print(f"hello ,{answer}")

b = get_int("b: ")
k = get_int("k: ")

print(b + k)

c = int(input("c: "))
m = int(input("m: "))

print(c - m)

x = int(input("x: "))
l = int(input("l: "))

print(x * l)

t = int(input("t: "))
m = int(input("m: "))

x = t / m
print(x)

m = int(input("m: "))
b = int(input("b: "))

v = m / b
print(f"{v:.32f}")

f = int(input("f: "))
k = int(input("k: "))

if (f < k):
    print("f is less than k")

elif (f > k):
    print("f is greater than k")

else:
    print("f and k are equal") 

b = input("b: ")
l = input("l: ")

if (b == l):
    print("same")

else: 
    print("different")

names = ["Ali","Jess","Cassandra"]
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

def sys_loop():
    print("system loop start from here")



sys_loop()


def sys_loop():
    while True:
        print("system loop starts from here")


sys_loop()


def formate_date():
    for i in range(3):
        print("date has been formatted")


formate_date()



def update_score():
    update_score = 0 
    while update_score < 3:
        update_score += 1
        print("score has been updated")



update_score()

def greet(name):
    print(f"hello, {name}")


greet("Natasha")    


def sys_loop():
    for i in range(3):
        update_score()




def update_score():
    print("score has been updated")            



sys_loop()

def odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

num = int(input("Enter your number: "))
print(f"The number {num} is {odd_or_even(num)}")    


def reverse_string(input_string):
    return input_string[::-1]


user_input = input("Enter your string: ")
print(f"The reverse string is {reverse_string(user_input)}")

def second_largest(numbers):
    unique_numbers = sorted(set(numbers),reverse=True)
    return unique_numbers[1]


num_list = [2,43,54,13,443,12]
print(f"The second largest number is {second_largest(num_list)}")

    














