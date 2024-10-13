

class Shape:
    def area(self):
        raise NotImplementedError("subclasses must overide this method")
class Rectangle(Shape):
   
    def area(self,length,width):
        return self.length*self.width
class Circle(Shape):
    def area(self,radius):
        return self.radius*self.radius*self.math.pi