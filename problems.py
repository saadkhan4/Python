# QUESTION: Write a Python function to check if a given number is odd or even.
def odd_or_even(number):
    if number % 2 == 0:             #This checks if the number is divisible by 2 without a remainder.
        return "Even"
    else:
        return "Odd"
    
num = int(input("Enter a number: "))
print(f"The number {num} is {odd_or_even(num)}")

# we used % sign because it will divide the number without giving remainder.
#if we used / (divide) sign, it will give us the remainder or decimal.