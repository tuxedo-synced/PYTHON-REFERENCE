# multiple inheritence - inherit from more than one parent class 
#                        C(A,B)

# multilevel inheritence = inherit from a parent which inherits from another parent 
#                           C(B) <- B(A) <- A

class Animal:
    def __init__(self,name):
        self.name = name 
    def eat(self):
        print(f"This {self.name} is eating .")

    def sleep(self):
        print(f"This {self.name} is sleeping .")

class Prey(Animal):
    def flee(self):
        print(f"this {self.name} is fleeking")

class Hunt(Animal):
    def hunt(self):
        print(f"this {self.name} is hunting")

class Rabbit(Prey):                                                 
    pass

class Python(Hunt):
    pass

class Fish(Prey,Hunt):              # multiple inheritence
    pass

rabbit = Rabbit("rabbit")
python = Python("python")
fish = Fish("fish")

rabbit.flee()
rabbit.eat()
rabbit.sleep()
python.hunt()
python.eat()
python.sleep()
fish.flee()
fish.eat()
fish.sleep()
fish.hunt()
fish.eat()
fish.sleep()

