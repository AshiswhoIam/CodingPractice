#Multiple - > child inherits from parent and Multilevel inheritance - > Child can inherit from parents parents

class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"The animal {self.name} is eating")
    def sleep(self):
        print(f"The animal  {self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"The animal  {self.name} is fleeing away")

class Predator(Animal):
    def hunt(self):
        print(f"The animal {self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit("BugsBunny")
hawk= Hawk("Rico")
fish=Fish("Nemo")

fish.eat()