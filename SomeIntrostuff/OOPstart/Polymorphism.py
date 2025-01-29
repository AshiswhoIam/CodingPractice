#in python polymorphism is achieved by inheritance "obj treated as same type as parent class"
#As well as duck typing -> obj must have necessary metyhods/attributes

from abc import ABC, abstractmethod

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__()

    def area(self):
        return 3.14*self.radius ** 2

class Square(Shape):
    def __init__(self,side):
        self.side=side
        super().__init__()

    def area(self):
        return self.side ** 2
    
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
        super().__init__()

    def area(self):
        return self.base *self.height* 0.5

class Pizza(Circle):
    def __init__(self,topping,radius):
        super().__init__(radius)
        self.topping=topping
     

shapes = [Circle(4),Square(5),Triangle(6,7),Pizza("Cheese",15)]


for shape in shapes:
    print(f"{shape.area()} cm^2")