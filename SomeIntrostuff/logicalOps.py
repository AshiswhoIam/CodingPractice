#or
temp=33
is_rain=False

if temp> 35 or temp <0 or is_rain:
    print("We are not going out")
else:
    print("We can head out")

#and
t=-5
is_sun=True

if t>= 28 and is_sun:
    print("It's hot fr fr ")
    print("It's sunny too")
elif t<=0 and is_sun:
    print("It's cold ")
    print("It's sunny too")
elif 28>t >0 and is_sun:
    print("It's warm ")
    print("It's sunny too")
#not

#conditonal exp
num=-5
a=6
b=7
age=21
print("Positive" if num>0 else "Negative")

re= "Even" if num%2 == 0 else "Odd"
print(re)

max_num = a if a>b else b
print(max_num)
min_num= a if a<b else b
print(min_num)

status= "Adult" if age>=18 else "Child"
print(status)


#Some string methods

name= input("enter name: ")
#result= len(name)
#print(result)
numba=input("enter #: ")

result=name.find("h")
#result=name.rfind("h")
#name=name.capitalize()
#name=name.upper()
#name=name.lower()
#isdigit() for checking if only digits bool,   isalpha for letters
print(result)
print(name)
rs=numba.count("-")
print(rs)
#numba=numba.replace("-", " ")


#Small exercise
#rules a name not more than 12 chars, no space, no digts.

user= input ("Enter user:")

if len(user)> 12 :
    print("Name cannot be more than 12 chars.")
elif not user.find(" ")==-1:
    print("Your user name cant have spaces")
elif not user.isalpha():
    print("No number should be in the name")
else:
    print(f"Hello {user}")



#accessing elements through []

number= "514-307-8179"
print(number[0])
print(number[0:4])
print(number[:4])
print(number[5:8])
print(number[5:])
print(number[-4])
#every 2nd chars
print(number[::2])

#last digits
last = number [-4:]
print(f"XXX-XXX-{last}")

#reversal
number= number[::-1]
print(number)
