#String
name ="Relearning variables"
#printout
print(name)
print(f"Using f string, My name is:{name}")

#Integers
age=456
age1=25
quantity=3

print(f"Using f string, My name is:{name} My age is:{age} years old")

#Float
price=12.78
print(f"the price is : ${price}")

#Boolean
is_grad = True
#if staments
if is_grad:
    print("You are a grad")
else:
    print("not a grad")


#TypeCasting
#retrieve var type
print(type(name))

price=int(price)
print(price)
age=float(age)
print(age)

age1=str(age1)
print(type(age1))

#user input
#age2 = int(input("Please enter age: ")) is another way
age2 = input("Please enter age: ")
#typecast
age2=int(age2)
#concat
age2=age2+1
print(f"You are {age2} ?")