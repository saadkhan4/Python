# concession stand program

menu = {
    "soda": 1.50,
    "water": 1.25,
    "chips": 2.00,
    "candy": 1.75,
    "cookie": 1.00
}

cart = []
total = 0

print("----- MENU -----")
for key, value in menu.items():
    print(f"{key:8}: {value:.2f}")

while True:
    food = input("Select an item to buy (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    
print("----- YOUR ORDER -----")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")    

