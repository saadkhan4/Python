# in this file we will learn how cs50 library works for you in python.

def get_int(prompt):
    while True:
           try:
            return int(input(prompt))
           except ValueError:
            pass
    
def main():
    x = get_int("x: ")
    y = get_int("y: ")

    print(x + y)

main()       




def get_int(prompt):
   while True:
      try:
         return int(input(prompt))
      except ValueError:
         pass
      
def main():
   x = int(input("x: "))
   y = int(input("y: "))

   print(x - y)

main()        