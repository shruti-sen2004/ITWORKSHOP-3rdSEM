# class variable - variables that are shared among all instances of a class
# instant variables are unique for each instance, class variable must be same 
# for all instances
class Employee: 
    raise_amount = 1.04
    total_employees = 0

    def __init__(self,first,last,pay): 
        self.first = first  
        self.last = last
        self.email= first + '.' + last + "@co.in"
        self.pay = pay

        Employee.total_employees +=1 # no instance based unique behaviour hence do not use self

    def fullname(self): # method
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self): # both instance and class can access it
        self.pay = int(self.pay * self.raise_amount) #can also do Employee.raise_amount; any subclass can override this val
        

emp_1 = Employee("Shruti","Sen",500000) # instance of class
emp_2 = Employee("Test","User",600000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# if an instance does not have the attribute it checks the parent or other class it inherits from has the same

emp_1.raise_amount = 1.05 # emp_1 now has a new attribute for raise
print(emp_1.__dict__) # print namespace of emp_1

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)
print(Employee.total_employees)