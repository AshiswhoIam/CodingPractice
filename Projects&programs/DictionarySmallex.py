#concession prg

menu={"pizza":3.00,
      "nachos":4.50,
      "popcorn": 6.00,
      "chips":2.99,
      "soda": 1.50
}


cart=[]

total=0

print("Menu")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("----------------")

while True:
    food= input("Choose an item q to quit: ").lower()
    if food == "q":
        break
    elif menu.get(food)is not None:
        cart.append(food)

print(cart)

for food in cart:
    total+= menu.get(food)
    print(food, end=" ")

print()
print(f"total is : ${total:.2f}")