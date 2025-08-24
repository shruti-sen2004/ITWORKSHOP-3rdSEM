# Property Decorator allows to define a method but access it like an attribute

class Employee: 
    def __init__(self,first,last):
        self.first = first  
        self.last = last

    @property            # similar to getter in java
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @property
    def email(self):
        return f'{self.first} {self.last}@co.in'

    @fullname.setter    # similar to setter in java
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter    
    def fullname(self):
        print("Name Delted!")
        self.first,self.last = None, None
        

emp_1 = Employee("Shruti","Sen") # instance of class

emp_1.first = "Jim"

emp_1.fullname = "Test User"
print(emp_1.fullname)
print(emp_1.email)

del emp_1.fullname