#poly besides inheritance. as long obj has att/methods

class Animal:
    alive=True

class Dog(Animal):
    def speak(self):
        print("woof")

class Cat(Animal):
    def speak(self):
        print("meow")

class Car:
    alive=False
    def speak(self):
        print("Honk")


animals = [Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)