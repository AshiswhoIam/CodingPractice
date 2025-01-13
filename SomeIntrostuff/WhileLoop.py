#skipped formatting went to while loops

passw = input("Enter your pass: ")

while passw =="":
    print("\nDid not enter it: ")
    passw = input("\nEnter your passw: ")
print(f"Your passw is {passw}")


car = input("Enter a car u like or L to leave: ")
while not  car  =="L":
    print(f"\n You have a preference of {car} ")
    car = input("\nEnter your pref car or L to leave: ")
print(f"You left")

number = int (input("enter a number b/w 1-20: "))

while number < 1 or number > 20:
    print(f"{number} is not appropriate")
    number = int (input("Enter a number b/w 1-20: "))
print(f"The num is {number}")