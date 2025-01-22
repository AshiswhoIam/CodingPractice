#iterable is obj/collection return element 1 at time


number = (1,2,3,4,5)

for item in reversed(number):
    print(number,end="  ")


#sets cant reverse obj cuz rules
fruit ={"apple","orange","banana","mango"}
for item in fruit:
    print(fruit,end="  ")

#string

name ="Ash"
for character in name:
    print(character, end=" ")

#dictionary
print()
di={"A":1,"B":2,"C":3}

for key, value in di.items():
    print(F"{key},{value}")

#Membership operators with string
print()
word="Mixer"
letter = input("guess a letter in the word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

# now with set

students= {"John", "Maddie","Tom"}

student= input("Enter name of st: ")
if student in students:
    print(f"There is a {student}")
else:
    print(f"{student} was not found")

#with dictionary
print()
grades = {"John":"A", "Maddie":"B","Tom":"F"}

user= input("Enter name of user: ")

if user in grades:
    print(f"There is a {user} with grades {grades[user]}")
else:
    print(f"{user} was not found")

#last ex

email = "john@gmail.com"

if"@" in email and "." in email:
    print("valid")
else:
    print("nop")


#List comprehension

doubles= [] 
for x in range(1,4):
    doubles.append(x*2)
print(doubles)

#make it easier with Lc
double = [x*2 for x in range(1,4)]
print(double)
fruits =["apple","orange","banana","mango"]
fruits=[fruit.upper() for fruit in fruits]
fruitchar=[fruit[0] for fruit in fruits]
print(fruits)
print(fruitchar)

#with conditiosn
print()
n= [1,3,-4,5,-7,-5,12]
p_n= [num for num in n if num>=0]
n_n= [num for num in n if num<0]
e_n= [num for num in n if num%2==0]
o_n= [num for num in n if num%2==1]

print(p_n)
print(n_n)
print(e_n)
print(o_n)

#another ex
print()
gd= [88,15,45,62,48,69]
passing= [g for g in gd if g >=60]
print(passing)