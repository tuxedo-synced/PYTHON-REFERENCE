#  static methods = A method that belong to a class rather than any object from that class (instance)
#                   Usually used for general utility functions

#  Instance methods = Best for operations on instances of the class (objects)
#  Static methods = Best for utility function that do not need access to class data 

class Employee:

    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_position = ["manager","casier","cook","hr"]
        return position in valid_position

# static methods do not have any contact with class data 
print(Employee.is_valid_position("manager"))
print(Employee.is_valid_position("Maharshi"))

# where instance methods do
emp = Employee("Rahul","berojgaar")
print(emp.get_info())
