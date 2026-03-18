# 4. Shape Area Calculator
# Create an abstract class Shape with:
#  Abstract method:
# o area()
# Create subclasses:
#  Circle
#  Rectangle
# Tasks:
# 1. Take input from the user (radius, length, breadth).
# 2. Calculate and display the area using appropriate class.
# 3. Explain why Shape is defined as an abstract class.


from abc import ABC,abstractmethod

class ABC:
    @abstractmethod
    def area_of_circle(self,radius):
        self.area  = 3.14*self.radius*self.radius
    @abstractmethod
    def area_of_rectangle(self,length,breath):
        self.area = length*breath
    def display(self,area):
        print(f"area of is {self.area}")

class circle:

    def __init__(self,radius):
         self.radius = radius
    def area_of_circle(self):
         self.area = 3.14*self.radius*self.radius
    def display(self):
        super().display(self.area)
        
class rectangle:

    def __init__(self,length,breath):
         self.length = length
         self.breath = breath
    def area_of_rectangle(self):
        self.area = self.length*self.breath      
    def display(self):
        super().display(self.area)


c1 = circle(2)
r1 = rectangle(3,4)

c1.area_of_circle()
c1.display()
