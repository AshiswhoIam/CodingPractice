
class Shape:
    def __init__(self,color,filled):
        self.color=color
        self.filled=filled

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.filled else"not filled"}")

class Circle(Shape):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled)
        self.radius=radius

    #method overidding
    def describe(self):
        print(f"It is a circle with area of {3.14*self.radius*self.radius} cm^2")
        #using the parents as well
        super().describe()

class Square(Shape):
    def __init__(self,color,filled,width):
        super().__init__(color,filled)
        self.width=width

    def describe(self):
        print(f"It is a square with area of {self.width*self.width} cm^2")
        #using the parents as well
        super().describe()

class Triangle(Shape):
    def __init__(self,color,filled,width,height):
        super().__init__(color,filled)
        self.width=width
        self.height=height

    def describe(self):
        print(f"It is a Triangle with area of {self.width*self.height/2} cm^2")
        #using the parents as well
        super().describe()

circle=Circle(color="red",filled=True,radius=5)
square=Square(color="blue",filled=False,width=3)
triangle=Triangle(color="black",filled=True,width=7,height=8)
print(circle.color)
print(circle.filled)
print(f"{circle.radius} cm")

print(square.color)
print(square.filled)
print(f"{square.width} cm ")

print(triangle.color)
print(triangle.filled)
print(f"{triangle.width} cm ")
print(f"{triangle.height} cm ")

circle.describe()

square.describe()

triangle.describe()
