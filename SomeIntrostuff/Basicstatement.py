#if statements

age= int(input("Enter age:"))
if age >=90:
    print("You are very old")
elif age >=18:
    print("You are an adult")
elif age<0:
    print("You are non existent")
else:
    print("You are below 18 above 0")


#another ex

ask= input("Do you want a meal?: (Yes/No)")
if ask =="Yes":
    print("Lets get u a meal")
elif ask =="":
    print("Nothing was typed")
else:
    print("guess you are not hungry")


