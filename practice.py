from cs50 import get_int , get_string

# answer = get_string("what's your name? ")
# print(f"hello , {answer}")

# answer = input("what's your name? ")
# print(f"hello , {answer}")


# x = get_int("x: ")
# y = get_int("y: ")

# print(x + y)

# x = int(input("x: "))
# y = int(input("y: "))

# print(x + y)

# s = int(input("s: "))
# u = int(input("u: "))

# z = s / u
# print(f"{z:.50f}")

# def system():
#     print("system is good")


# system()

# def system():
#     for system in range(4):
#         print("system is good")


# system()        

# def system():
#     system = 0
#     while system < 3:
#         system += 1
#         print("system is good")


# system()        

# scores = []
# for i in range(3):
#     score = get_int("Score: ")
#     scores.append(score)

# average = sum(scores) / len(scores)
# print(f"average: {average}")    


names = ["Iqbal" , "Hamza" ,"Ali"]
name = get_string("Name: ")
if name in names:
    print("found")

else:
    print("not found")



