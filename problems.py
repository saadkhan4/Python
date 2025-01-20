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
def second_largest(numbers):
    unique_number = sorted(set(numbers), reverse=True)   #	set(numbers) converts the list to a set, which removes duplicate values. ###sorted(..., reverse=True) sorts the unique numbers in descending order (largest to smallest).
    return unique_number[1]                              #  unique_numbers[1] retrieves the second element from the sorted list.

num_list = [10, 20, 4, 45, 99, 99] 
print(f"The second largest number is {second_largest(num_list)}")
