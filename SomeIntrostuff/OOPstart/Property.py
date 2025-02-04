#read,write,del att its a decorator
#getter,setter,del


class Rectangle:

    #_ is protected method
    def __init__(self,width,height):
        self._width=width
        self._height=height

    @property
    def width(self):
        return f"{self._width:.1f} "

    @property
    def height(self):
        return f"{self.height:.1f} "
    
    @width.setter
    def width(self,new_width):
        if new_width>0:
            self._width=new_width
        else:
            print("Width must be greater than 0")
    @height.setter
    def height(self,new_height):
        if new_height>0:
            self._height=new_height
        else:
            print("height must be greater than 0")
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")
    
rect=Rectangle(3,4)

rect.width=5
rect.height=6

del rect.width
del rect.height

#print(rect._width)
#print(rect._height)

