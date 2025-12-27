# Inheritence = Allow a class to inherit attributes and methods from another class 
#               Helps with code reusability and extensibility 
#               Class Chils(Parent)

class Animal:
    def __init__(self,name,food):
        self.name = name 
        self.food = food
    def namew(self):
        print(f"Animal name is {self.name}")
    def foodw(self):
        print(f"Animal food is {self.food}")

class Cat(Animal):
    pass
 
class Dog(Animal):
    pass
 
class Tiger(Animal):
    pass
 
class Lion(Animal):
    pass
 
class Goat(Animal):
    pass

a = Cat("Kitty","Cat Food")
a.namew()
a.foodw()

print(end="\n\n\n")
 
