import math

class Shape:
    def area(self):
        raise NotImplementedError("subclasses must overide this method")
class Rectangle(Shape):
    def __init__(self,length,width):
        self,length = length
        self.width = width
    def area(self,length,width):
        return self.length*self.width
class Circle(Shape):
    def __init__(self,radius):
        self,radius = radius
       
    def area(self,radius):
        return self.radius*self.radius*self.math.pi