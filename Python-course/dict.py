# dictionary = a collection of {key:value} pairs ordered and unchangeable.

capitals = {"USA": "Washington D.C", "South Korea": "Seoul", "England": "London", "France": "Paris"}

print(capitals.get("USA"))   # finding from print function.
# .get() method allows you to check if a key is in dictionary.

# Finding from conditional statement.

if capitals.get("South Korea"):
    print("That capital exists")
else:
    print("That capital doesn't exist")    

capitals.update({"Japan": "Tokyo"})    # add the key-value pair
capitals.update({"USA": "Las Vegas"})  # update the key-value pair
print(capitals)
# .update() method allows you to insert a new key-value pair or update an existing one.

capitals.pop("France")
print(capitals)
# .pop() method allows you to remove a key-value pair.
# .clear() method allows you remove every key-value pair from dictionary.

capitals.popitem()                        # this allow you remove the latest key-value pair from dictionary.
print(capitals)

for key, value in capitals.items():
    print(f"{key}: {value}")               # to print every key-value pair.
 
#.items() method is used with dictionaries, and it returns each key-value pair as a tuple.