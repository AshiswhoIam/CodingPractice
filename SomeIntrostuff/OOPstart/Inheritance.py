class Animal:
    def __init__(self, name):
        self.name=name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")



class Dog(Animal):
    print()
    def speak(self):
        print("Woof")

class Cat(Animal):
    print()
    def speak(self):
        print("Meow")

class Mouse(Animal):
    print()
    def speak(self):
        print("squeaky")

dog = Dog("Scoobydoo")
cat= Cat("Garfield")
mouse = Mouse("Jerry")

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()
dog.speak()
mouse.speak()
cat.speak()