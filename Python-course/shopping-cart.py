# SHOPPING CART PROGRAM

item = input("What item would you like to buy?: ")
price = float(input("What's the price?: "))
quantity = int(input("How much do you want?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")
