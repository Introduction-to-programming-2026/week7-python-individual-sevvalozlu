# Project 5 — Mini Shopping Cart
# Author: Şevval Özlü

menu = {
    1: ("Apple",  0.50),
    2: ("Banana", 0.30),
    3: ("Milk",   1.20),
    4: ("Bread",  2.00),
}

cart  = {}    { item_name: quantity }
total = 0.0

# TODO: display the menu
print("--- Shop Menu ---")
 for number, (name, price) in menu.items():
     print(f"{number}. {name:<10} ${price:.2f}")
print("5. Done")

# shopping loop
while True:
     choice = int(input("\nChoose an item (1-5): "))
    if choice == 5:
        break
     if choice in menu:
         name, price =menu[choice]
         
# BONUS: ask how many
 quantity = int(input("How many?: "))

 if name in cart:
     cart[name] += quantity
 else:
     cart[name] = quantity
     
    total += price * quantity
    print(f"Added {name}. Total: ${total:.2f}")
else:
   print("Invalid choice, try again.")
     
#         ...add to cart, update total...
#     else:
#         print("Invalid choice, try again.")

# TODO: print the receipt
#BONUS: apply 10% discount if total > 5
if total > 5:
    total *= 0.9
print("\n--- Receipt ---")
 for item, qty in cart.items():
     price = 0
     for _, (n, p) in menu.items():
         if n == item:
             price = p
    print(f"item} x{qty} ${price * qty:.2f}")
print("____________________")
print(f"Total: ${total:.2f}")
print("Thank you!")
