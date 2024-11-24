#using dict
# people = [
#     {"name": "Margot", "number": "0324-5454543"},
#     {"name": "Jennifer","number": "0343-1232223"},
#     {"name":  "Agatha" , "number": "0565-3434322"},
# ]

# name = input("Name: ")

# for person in people:
#     if person["name"] == name:
#         number = person["number"]
#         print(f"Found {number}")
#         break
# else:
#     print("not found")    

# different way

people = {
    "Margot": "0324-5454543",
    "Jennifer":"0343-1232223",
    "Agatha":"0565-3434322",
}

name = input("Name: ")

if name in people:
    number = people[name]
    print(f"found {number}")
else:
    print("not found")    

