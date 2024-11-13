#Ex 1 rectangle calc

length = float(input("Enter length:"))
width = float(input("Enter width:"))

area = length*width

print(f"The area is: {area}dm^2")

#Ex2 Buy Cart

item = input("\nEnter item u want to buy:")
price= float(input("\nhow much does it cost:"))
quantity= int(input("\nhow many is needed?"))
total = price*quantity

print(f"\nThe total is: {total} you bought {quantity} {item}")