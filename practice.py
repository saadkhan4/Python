from cs50 import get_string , get_int

scores = []
for i in range(3):
    player = int(input("Score: "))
    scores.append(player)

average = sum(scores) / len(scores)
print(f"Average: {average}")


def scorecard():
    print("scorecard has been updated")


scorecard()


def system():
    while True:
        print("system malfunctioning")


system()


def sys_loop():
    for i in range(3):
        print("loop started from here")



sys_loop()


def scorecard():
    scorecard = 0
    while scorecard < 3:
        scorecard += 1
        print("scorecard is updated")



scorecard()



def greet(name):
    print(f"hello , {name}")



greet("Natasha") 


def sys_loop():
    for i in range(3):
        system()



def system():
    print("system malfunctioning")        




sys_loop()



def odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
num = int(input("Enter your number: "))
print(f"The number {num} is {odd_or_even(num)} ")    


def reverse_string(input_string):
    return input_string [::-1]

user_input = input("Enter your string: ")
print(f"The reverse string is {reverse_string(user_input)}")

def second_largest(numbers):
    unique_numbers = sorted(set(numbers),reverse=True)
    return unique_numbers[1]


num_list = [12,42,2134,131,11]
print(f"The second largest number is {second_largest(num_list)}")










