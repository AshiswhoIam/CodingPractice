#default args 
import time

def price(ini,discount=0,tax=0.05):
    return ini*(1-discount)*(1+tax)

print(price(500))
print(price(500,0.1))
print(price(500,0.1,0))


def count(s,e):
    for x in range(s , e+1):
        print(x)
        time.sleep(1)
    print("done")

count(0,2)


#key word args

def hello(greet,title,f,l):
    print(f"{greet}{title}{f}{l}")

hello("Hello " ,"Mr" ,"Spongebob", "squarepants")
hello("Hello " ,title="Mr" , l="squarepants",f="Spongebob")

#priting numbers end is key word arg
for x in range(1,6):
    print(x,end=" ")

#function to gen a phone num
print()
def get_phone(country,area,f,l):
    return f"{country}-{area}-{f}-{l}"

phone_num= get_phone(country=1,area=123,f=546,l=1231)
print(phone_num)
print()

#args i think like tuples

def add(*args):
    total=0
    for arg in args:
        total+=arg
    return total
print(add(1,2,3))


def display_name(*args):
    for arg in args:
        print(arg, end= " ")

display_name("DR","John","babayega","wick")
print()
#kwargs like dictionary
def addy(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

addy(street="allyway 321",
     city="wakanda",
     province="avengy",
     zip="X7A 6T1")


# args and kwargs together

def label(*args,**kwargs):
    for arg in args:
        print(arg, end= " ")
    print()
    for value in  kwargs.values():
        print(value,end =" ")

    #can also do like print(f"{kwargs.get('street')}")
print()
label("DR","John","babayega","wick",
    street="allyway 321",
     city="wakanda",
     province="avengy",
     zip="X7A 6T1")

