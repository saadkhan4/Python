before = input("Before: ")
print("After:  ", end="")  # what implies is default is "\n". 
for c in before:
    print(c.upper(), end="")
print()



before = input("Before: ")
print("After: " , end="")     # this is operational parameter. end=""
for c in before:
    print(c.upper(),end="")     
print()    



# or you can this way too

before = input("Before: ")
print("After:  ", end="")
print(before.upper()) 

# this way too

# before = input("before: ")
# after = before.upper()
# print(f"After: {after}")

