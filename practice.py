from cs50 import get_string , get_int

# answer = input("what's your name? ")
# print(f"hello ,{answer}")

# answer = get_string("what's your name? ")
# print(f"hello ,{answer}")

# v = get_int("v: ")
# t = get_int("t: ")

# print(v + t)

# c = int(input("c: "))
# p = int(input("p: "))

# print(c - p)

# x = int(input("x: "))
# q = int(input("q: "))

# print(x * q)


# r = int(input("r: "))
# w = int(input("w: "))

# print(r / w)

# q = int(input("q: "))
# k = int(input("k: "))

# r = q / k
# print(r)


# d = int(input("d: "))
# l = int(input("l: "))

# g = d / l
# print(f"{g:.43f}")

# k = int(input("k: "))
# o = int(input("o: "))

# if (k < o):
#     print("k is less than o")

# elif (k > o):
#     print("k is greater than o")

# else:
#     print("k and o are equal")

            
# s = input("s: ")
# p = input("p: ")

# if s == p:
#     print("same")

# else: 
#     print("different") 



# names = ["Ali","Megan","Cassandra"]
# name = input("name: ")

# if name in names:
#     print("found")

# else:
#     print("not found")


# scores = []
# for i in range(3):
#     player = int(input("score: "))
#     scores.append(player)

# average = sum(scores) / len(scores)
# print(f"Average: {average}")   

   
   
# def system():
#     print("system is malfunctioning")


# system()


# def sort_array():
#     for i in range(4):
#         print("array has been started")


# sort_array()


# def delete_file():
#     while True:
#         print("file has been deleted")


# delete_file()



# def sys_loop():
#     sys_loop = 0
#     while sys_loop < 3:
#         sys_loop += 1
#         print("loop start from here")


# sys_loop()        


# def greet(name):
#     print(f"hello , {name}")


# greet("Natasha")

# def main():
#     for i in range(3):
#         sys_loop()



# def sys_loop():
#     print("loop has been initialized") 



# main()          

# def odd_or_even(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
    

# num = int(input("Enter your number: "))
# print(f"The num {num} is {odd_or_even(num)}")

# def reverse_string(input_string):
#     return input_string [::-1]

# user_input = input("Enter your string: ")
# print(f"The reverse string is {reverse_string(user_input)}")


# def second_largest(numbers):
#     unique_number = sorted(set(numbers),reverse=True)
#     return unique_number[1]


# num_list = [34,34,56,76,88,98,12,54]
# print(f"The second largest number is {second_largest(num_list)}")

# def find_duplicates(numbers):
#     duplicates = []
#     seen = set()

#     for num in numbers:
#         if num in seen and num not in duplicates:
#             duplicates.append(num)
#         seen.add(num)

#     return duplicates

# num_list = [1,4,2,5,6,7,8,9,3,4,5,1,7,2,9,4]
# print(f"Duplicate numbers: {find_duplicates(num_list)}")



def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

print(are_anagrams("Listen", "Silent"))
print(are_anagrams("Hello", "World"))











            












