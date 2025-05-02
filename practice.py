from cs50 import get_string , get_int

answer = get_string("what's your name? ")
print(f"hello ,{answer}")

answer = input("what's your name? ")
print(f"hello ,{answer}")

c = get_int("c: ")
p = get_int("p: ")

print(c + p)

v = int(input("v: "))
k = int(input("k: "))

print(v - k)

t = int(input("t: "))
o = int(input("o: "))

b = t / o
print(b)

q = int(input("q: "))
i = int(input("i: "))

print(q * i)

y = int(input("y: "))
p = int(input("p: "))

g = y / p
print(f"{g:.43f}")

x = int(input("x: "))
l = int(input("l: "))

if (x < l):
    print("x is less than l")

elif(x > l):
    print("x is greater than l")

else:
    print("x and l are equal") 

o = input("o: ")
k = input("k: ")

if (o == k):
    print("same")

else:
    print("different")    

names = ["Megan", "Ali", "Sara"]
name = input("Name: ")

if name in names:
    print("Found")

else:
    print("Not found") 

scores = []
for i in range(3):
    player = int(input("Scores: "))
    scores.append(player)

average = sum(scores) / len(scores)
print(f"Average: {average}")    

def sys_loop():
    while True:
       print("loop has been started")

sys_loop()

def machine():
    for i in range(3):
        print("machine is malfunctioning")

machine()

def sys_loop():
    sys_loop = 0
    while sys_loop < 3:
        sys_loop += 1 
        print("system loop started from here")


sys_loop()         

def greet(name):
    print(f"hello, {name}")

greet("Natasha")

def sys_info():
    for i in range(3):
        machine()


def machine():
    print("info is confidential")        

sys_info()

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

def second_largest(number):
    unique_number = sorted(set(number),reverse=True)
    return unique_number[1]

num_list = [23,43,34,87,12,90,22]
print(f"The second largest number is {second_largest(num_list)}")

def find_Duplicates(numbers):
    duplicates = []
    seen = set()

    for num in numbers:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        seen.add(num)

    return duplicates

num_list = [1,4,5,1,7,4]
print(f"Duplicate numbers: {find_Duplicates(num_list)}")        

def are_anagrams(str1,str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

print(are_anagrams("Silent", "Listen"))
print(are_anagrams("Hello", "World"))

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Education is power"))        

def word_length(word_list):
    word_dict = {}
    for word in word_list:
        word_dict[word] = len(word)
    return word_dict

words = ["Khan", "Charlotte", "Bob"]
print(word_length(words))  







