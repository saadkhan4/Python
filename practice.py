from cs50 import get_string , get_int

reply = input("What's your company? ")
print(f"It's {reply}")

answer = get_string("what's your name? ")
print(f"hello {answer}")

p = int(input("p: "))
b = int(input("b: "))

print(p + b)

f = int(input("f: "))
k = int(input("k: "))

print(f - k)


v = int(input("v: "))
o = int(input("o: "))

print(v * o)

c = int(input("c: "))
d = int(input("d: "))

z = c / d
print(z)

q = int(input("q: "))
l = int(input("l: "))

r = q / l 
print(f"{r:.40f}")

x = int(input("x: "))
m = int(input("m: "))

if (x < m):
    print("x is less than m")
elif (x > m):
    print("x is greater than m")
else:
    print("x and m are equal")    
    
s = input("s: ")
h = input("h: ")

if (s == h):
    print("same")
else:
    print("different")


temp = int(input("What's the temperature? "))

if (temp >= 35):
    print("It's very hot today.")
elif (temp >= 20):
    print("It's moderate today.")
else:
    print("It's cold today.")       

names = ["Charlotte", "John", "Anna"]
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


def sys_loop():
    while True:
        print("it keeps going....")

sys_loop()

def for_loop():
    for i in range(3):
        print("This is for loop.")

for_loop()        

def sys_loop():
    sys_loop = 0
    while sys_loop < 3:
        sys_loop += 1
        print("This is while loop.")


sys_loop()        

def greet(name):
    print(f"Hello ,{name}")

greet("Natasha")

def system():
    for i in range(3):
        sys_loop()


def sys_loop():
    print("This is nested function.") 


system()

def odd_or_even(number):
    if number % 2 == 0:
        return "Odd"
    else:
        return "Even"
    
num = int(input("Enter your number: "))
print(f"The number {num} is {odd_or_even(num)}")    

def reverse_string(input_string):
    return input_string [::-1]

user_input = input("Enter your string: ")
print(f"The reverse string is {reverse_string(user_input)}")

def second_largest(numbers):
    unique_number = sorted(set(numbers),reverse=True)
    return unique_number [1]

num_list = [32,12,54,23,12,2,5,90]
print(f"The Second largest number is {second_largest(num_list)}")

def find_duplicates(numbers):
    duplicates = []
    seen = set()

    for num in numbers:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        seen.add(num)

    return duplicates 

num_list = [14,36,44,22,44,12,12,34,23,32]
print(f"Duplicate numbers: {find_duplicates(num_list)}")        

def are_anagrams(str1,str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

print(are_anagrams("Listen", "Silent"))
print(are_anagrams("Hello", "World"))

def count_vowels(text):
    vowels = "AEIOUaeiou"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("system is malfunctioning"))

def word_length(word_list):
    word_dict = {}
    for word in word_list:
        word_dict[word] = len(word)
    return word_dict

words = ["Charlotte", "Anna", "Scarlet"]    
print(word_length(words))


