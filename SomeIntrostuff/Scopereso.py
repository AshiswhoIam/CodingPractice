#fnc cant see in another fncs, variable scope->visi and access
#  .. sr->local enc glob uilt inc

#local
def fnc1():
    x=1
    print(x)

def fnc2():
    x=2
    print(x)

fnc1
fnc2

#enclosed later


#global
y=2
def func1():
    print(y)

def func2():
    print(y)

#built in
from math import e

def f1():
    print(e)
e=3

f1()



#def main():
#    print()
#if __name__ == '__main__':
#    main()