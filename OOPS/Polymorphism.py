# Polymorphism = Greek word that means to "have many forms or faces"
#                Poly -> Many
#                Morphe -> Form

#                TWO WAYS TO ACHIEVE POLYMORPHISM
#                1. Inheritance = An object could be treated of the same type as a parent class .
#                2. "Duck typing" = Object must have necessary attributes/methods .

from abc import ABC, abstractmethod
import math

class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(f"Area of circle with radius {self.radius} = {(math.pi)*(self.radius ** 2)}")

class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        print(f"Area of square with side {self.side} = {self.side ** 2}")

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        print(f"Area of circle with base {self.base} and height {self.height} = {0.5*self.base*self.height}")

class Pizza(Circle):
    def __init__(self,toppings,radius):
        super().__init__(radius)
        self.toppings = toppings
    def area(self):
        print(f"The pizza's area with radius {self.radius} and toppings {self.toppings} is = {(math.pi)*(self.radius ** 2)}")

shapes = [Circle(4),Square(4),Triangle(4,2),Pizza("Mozorilla",4)]

for i in shapes:
    print(i.area())

# Note:- u are calling a method with no return value so it returns None , when ur printing it (ie ., print(i.area())) , The  none returned is printed .
