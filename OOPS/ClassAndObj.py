# object = A "bundle" of related attributes (variables) and methods (functions) 
#          Ex. phone , cup , book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object .

# function defined inside class is called a method .

# syntax for a class :-
# class class_name:
#     variable1
#     variable2
#         .
#         .
#     variable
#     def __init__(self,parameter1,parameter2,...):
#           self.variable1 = parameter1
#           self.variable2 = parameter2
#           self.variable3 = parameter3
#     method1()
#     method2()
#         .
#         .
#     method()

class Car:
    def __init__(self , speed):
        self.speed = speed
    def start(self):
        self.speed+=1
        print("Car started .")
    def speedw(self):
        print(f"speed of car is {self.speed}")
    def accelerate(self):
        self.speed+=1
    def deaccelerate(self):
        self.speed-=1
    def stop(self):
        if self.speed == 0:
            print("Car stopped .")
        else:
            print("Cannot stop ,Deaccelerate the car .")

car1 = Car(0)
car1.start()
car1.speedw()
car1.accelerate()
car1.speedw()
car1.deaccelerate()
car1.speedw()
car1.stop()
car1.deaccelerate()
car1.speedw()
car1.stop()
car2 = Car(5)

# class variables = Shared among all instances of a class .
#                   Defined outside the constructer .
#                   Allow you to share data among all objects treated from the class .


class Students:
    numStudents = 0 
    def __init__(self):
        Students.numStudents+=1
    def total(self):
        print(f"students present {numStudents}")
    
std1 = Students()
std2 = Students()
std3 = Students()
std4 = Students()
print(Students.numStudents)
print(std1.numStudents)
print(std2.numStudents)
print(std3.numStudents)
