from cs50 import get_int
 
# conditional code. 

x = get_int("what's x? ")
y = get_int("what's y? ")

if x < y:
    print("x is less than y")
elif x > y:                         
    print("x is greater than y")
else:
    print("x is equal to y")   
     
 
# now we are comparing strings. 

s = input("s: ")
t = input("t: ")

if s == t:
    print("Same")
else:
    print("Different")
    
# this is how you compare strings without strcmp in python.    
