#fnc that extends behavior of another fnc
#doesnt modify base fnc passes it as arg to dec


#deco
#wrapper so that statements is there for only when we call the mehtods
def add_sugar(fnc):
    def wrapper(*args,**kwargs):
        print("Adding the sugar ! ! !")
        fnc(*args,**kwargs)
    return wrapper

def add_salt(fnc):
    def wrapper(*args,**kwargs):
        print("Adding the salt ! ! !")
        fnc(*args,**kwargs)
    return wrapper


@add_sugar
@add_salt
def get_ice(flavor):
    print(f"Here is your {flavor} ice")

get_ice("choco")