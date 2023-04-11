# Define a class named Rectangle which inherits from Shape class from task 2.
# Class instance can be constructed by a length and width. 
#The Rectangle class has a method which can compute the area.


class Shape():
    def __init__(self, l, w):
        self.l = int(input())
        self.w = int(input())
    def area(self):
        print(self.l * self.w)
class Rectangle(Shape):
    def __init__(self, l, w):
        Shape.__init__(self, l, w)

x=Rectangle(l =, w =)
x.area()

