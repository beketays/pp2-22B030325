# Define a class named Shape and its subclass Square. 
#The Square class has an init function which takes a length as argument. 
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape():
    def __init__(self, l):
        self.l = int(input())
    def area(self):
        print(self.l**2)
class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self, l)
        
x=Square(Shape)
x.area()    

