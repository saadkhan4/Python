#vertical method for printing (#). 
from cs50 import get_int


while True:                  # there is no do while loop in python so this is forever loop in python.
    n = get_int("Height: ")
    if n > 0:
        break

for i in range(n):
    print("#")   


# ^^^ horizontal method for Printing(#).^^^
# bunch of ways here to do this.

print("?" * 4)      # easy way.




# ^^^^^ now nested loop to print 3x3 block .^^^^^
for i in range(3):
    for j in range(3):
        print("#" , end="")
    print()    


# this way too

for i in range(3):
    print("#" * 3)     