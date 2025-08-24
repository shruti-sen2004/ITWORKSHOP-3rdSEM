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
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #can also do Employee.raise_amount; any subclass can override this val

# Inherits all attributes of Employee class 
class Developer(Employee): 
    raise_amount = 1.10   # makes changes w/o effecting parent class
    def __init__(self,first,last,pay,prog_lang): 
        super().__init__(first,last,pay)  # prefer this over Employee.__init__
        self.prog_lang = prog_lang

class Manager(Employee):   
    def __init__(self,first,last,pay,employees= None): # don't pass mutable datatypes as arguments
        super().__init__(first,last,pay)  
        if employees is None:
            self.employees = []
        else:
            self.employees= employees
    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())

dev_1 = Developer("Shruti","Sen",500000,"Python") # instance of class
dev_2 = Developer("Test","User",600000,"Java")
# print(dev_1.prog_lang)
# print(dev_2.prog_lang)

mgr_1 = Manager("Sue","Smith", 900000,[dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()


# print(help(Developer)) # can display Method resolution order

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

print(isinstance(mgr_1,Manager))
print(isinstance(mgr_1,Employee))
print(isinstance(mgr_1,Developer))

print(issubclass(Manager,Employee))
print(issubclass(Manager,Developer))