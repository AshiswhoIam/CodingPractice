#functions

def looper(name,age):
    print(f"Loop 3x {name}")
    print(f"You are aged at {age}")

looper("ash",20)
looper("E",94)
looper("Mc",56)


#another
def display_in(name,amount,due):
    print(f"Hello {name}")
    print(f"You bill amount of {amount} due at {due}")

display_in("ash",124.01,"01/30/2025")


#return statement

def add(x,y):
    z=x+y
    return z

def sub(x,y):
    z=x-y
    return z

print(add(1,5))
print(sub(12,5))

#
def create_name(f,l):
    f= f.capitalize()
    l= l.capitalize()
    return f+ " " +l

full = create_name("john","don")

print(full)
