#user input exercise
# username is no more than 12 characters]
# username must not contain digits
# username must not contain spaces

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")

elif not username.isalpha():
    print("Your username can't contain numbers")        #	username.isalpha() → ensures only letters (no digits, no spaces, no symbols).

else: 
    print(f"Welcome {username}")   