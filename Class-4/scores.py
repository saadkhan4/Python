scores = [72 , 46 , 90]

average = sum(scores) / len(scores)

print(f"Average: {average}")


from cs50 import get_int

scores = [] 
for i in range(3):
     scores = get_int("Scores: ")
     scores.append(scores)

average = sum(scores) / len(scores)
print(f"Average: {average}")     

