#python calc

ops = input("Enter the op (+ - * /)")
num = float(input("enter 1st num:"))
num1 = float(input("enter 2nd num:"))

if ops== "+":
    r= num+num1
    print(r)
elif ops== "-":
    r= num-num1
    print(r)
elif ops== "*":
    r= num*num1
    print(r)
elif ops== "/":
    r= num/num1
    print(r)
else:
    print(f"{ops} is not a val op")

#  print(round(r,3)) round is to round 3 is for 3 digits after deicimal


#Weight conversion
w= float(input("\nenter weight: "))
unit= input("\nEnter kg or lbs: ")

if unit== "kg":
    w =w * 2.205
    unit="lbs."
    print(f"\nYour weight is: {w} in {unit} ")
elif unit== "lbs":
    w =w / 2.205
    unit="kgs."
    print(f"\nYour weight is: {w} in {unit} ")
else:
    print(f"{unit} is not valid")

#Temp conversion


u= input("\n Decide if temp is in C or F ")
temp= float(input("\nEnter Temp: "))

if u =="C":
    temp= round((9*temp)/5+32,1)
    print(f"\nYour temp in F is: {temp} ")
elif u=="F":
    temp=round((temp-32)*5/9,1)
    print(f"\nYour temp in C is: {temp} ")
else:
     print(f"\n{u} is invalid ")