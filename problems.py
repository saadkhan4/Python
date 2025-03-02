# # QUESTION: Write a Python function to check if a given number is odd or even.
# def odd_or_even(number):
#     if number % 2 == 0:             #This checks if the number is divisible by 2 without a remainder.
#         return "Even"
#     else:
#         return "Odd"
    
# num = int(input("Enter a number: "))
# print(f"The number {num} is {odd_or_even(num)}")

# # we used % sign because it will divide the number without giving remainder.
# # if we used / (divide) sign, it will give us the remainder or decimal.


# # QUESTION: Write a Python function that takes a string as input and returns the string reversed.
# def reverse_string(input_string):
#     return input_string[::-1]       #[::-1] means “take the entire string but step backwards by 1”.

# user_input = input("Enter a string: ")
# print(f"The reverse string is {reverse_string(user_input)}")

#QUESTION: Write a Python function to find the second largest number in a list. Assume the list contains at least two unique numbers.
# def second_largest(numbers):
#     unique_number = sorted(set(numbers), reverse=True)   #	set(numbers) converts the list to a set, which removes duplicate values. ###sorted(..., reverse=True) sorts the unique numbers in descending order (largest to smallest).
#     return unique_number[1]                              #  unique_numbers[1] retrieves the second element from the sorted list.

# num_list = [10, 20, 4, 45, 99, 99] 
# print(f"The second largest number is {second_largest(num_list)}")

#QUESTION:-Data Structures:
# You are given a list of integers where some numbers appear more than once. Write a Python function to return a list of duplicates.
# def find_duplicate(numbers):
#     duplicates = []       #Stores duplicate numbers.
#     seen = set()          #Tracks numbers that have already appeared.

#     for num in numbers:
#         if num in seen and num not in duplicates:    #num not in duplicates → Ensures we don’t add the same duplicate multiple times.
#             duplicates.append(num)
#         seen.add(num)     #stores numbers that have appeared.

#     return duplicates

# num_list = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 3]
# print(f"Duplicate numbers: {find_duplicate(num_list)}")
#QUESTION:-
# Logical Problem:
# Write a Python function to check if two strings are anagrams of each other. Ignore spaces and capitalization.             
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if sorted characters are the same
    return sorted(str1) == sorted(str2)

# Example usage
print(are_anagrams("Listen", "Silent"))  # Output: True
print(are_anagrams("Hello", "World"))    # Output: False


# def are_anagrams(str1, str2):
#     str1 = str1.replace(" ", "").lower
#     str2 = str2.replace(" ", "").lower

#     return sorted(str1) == sorted(str2)

# print(are_anagrams("Listen", "Silent"))
# print(are_anagrams("Hello", "World"))



    

