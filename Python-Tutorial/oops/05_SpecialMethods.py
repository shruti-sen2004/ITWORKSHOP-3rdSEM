# Special Methods are used to change the inbuit behaviour of a function 
# Can help in object specific behaviour and operator overloading

class Employee: 
    raise_amount = 1.04
    total_employees = 0

    def __init__(self,first,last,pay): # dunder init -> init surounded by double underscore
        self.first = first  
        self.last = last
        self.email= first + '.' + last + "@co.in"
        self.pay = pay

        Employee.total_employees +=1 

    def fullname(self): # method
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 

    # atleast have this - display something which can be copied to recreate same object
    def __repr__(self): # unambiguous representation of an object, meant to seen for other devs
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)

    def __str__(self): # readable representation of an object to be seen by user
        return f"{self.fullname()} - {self.email}"
     
    def __add__(self,other): # operator overloading
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
        

emp_1 = Employee("Shruti","Sen",500000) 
emp_2 = Employee("Test","User",600000)
print(emp_1 + emp_2)
print(len(emp_1))

# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(int.__add__(1,2))
# print(str.__add__('a','b')) # add
# print("test".__len__()) # len

'''
NOTE : 
Python does not support method overloading like java or c++ (it is dynamically typed it becomes unnecessary)
In python, if multiple methods with same names are defined, the last defination will overwrite the previous ones.

But similar functionality can be achieved using :

Method-1 : Default Argumnts
class Example:
    def greet(self, name="Guest"):
        print(f"Hello, {name}!")
obj = Example()
obj.greet()          # Output: Hello, Guest!
obj.greet("Alice")   # Output: Hello, Alice!

Method-2 : Using *args and **kwargs for variable no.of args
class Example:
    def greet(self, *args):
        if len(args) == 0:
            print("Hello, Guest!")
        elif len(args) == 1:
            print(f"Hello, {args[0]}!")
        else:
            print("Hello, everyone!")
obj = Example()
obj.greet()                  # Output: Hello, Guest!
obj.greet("Alice")           # Output: Hello, Alice!
obj.greet("Alice", "Bob")    # Output: Hello, everyone!

Method-3 : Type checking
class Example:
    def greet(self, name):
        if isinstance(name, str):
            print(f"Hello, {name}!")
        elif isinstance(name, list):
            print(f"Hello, {', '.join(name)}!")
        else:
            print("Invalid input!")
obj = Example()
obj.greet("Alice")           # Output: Hello, Alice!
obj.greet(["Alice", "Bob"])  # Output: Hello, Alice, Bob!
obj.greet(123)               # Output: Invalid input!

'''