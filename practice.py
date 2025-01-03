from cs50 import get_string , get_int

# answer = get_string("what's your name? ")
# print(f"hello , {answer}")


# answer = input("what's your name? ")
# print(f"hello , {answer}")


# e = get_int("e: ")
# f = get_int("f: ")

# print(e + f)

# f = int(input("f: "))
# d = int(input("d: "))

# print(f + d)

# d = int(input("d: "))
# t = int(input("t: "))

# q = d / t
# print(f"{q:.34f}")

# x = get_int("x: ")
# r = get_int("r: ")

# if (x < r):
#     print("x is less than r")

# elif (x > r):
#     print("x is greater than r")
    
# else :
#     print("x is equal to r")        

# def system():
#     print("system is good")


# system()


# def system():
#     for system in range(3):
#         print("system is good")


# system()

# def system():
#     system = 0
#     while system < 3:
#         system += 1
#         print("system is good")



# system()        


scores = []
for i in range(3):
    score = get_int("Score: ")
    scores.append(score)

average = sum(scores) / len(scores)
print(f"Average: {average}")    


