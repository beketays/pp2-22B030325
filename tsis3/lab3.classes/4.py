''' Write the definition of a Point class. Objects from this class should have a

a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points
'''
import math
class pclass():
    def __init__(self):
        self.x = int(input())
        self.y = int(input())

    def show(self):
        print(self.x, self.y)

    def move(self):
        x1=int(input())
        y1=int(input())
        self.x=self.x+x1
        self.y=self.y+y1 
        print(self.x, self.y)
    
    def distan(self):
        print(math.sqrt(self.x**2+self.y**2))

p1=pclass(input())
p1.show()