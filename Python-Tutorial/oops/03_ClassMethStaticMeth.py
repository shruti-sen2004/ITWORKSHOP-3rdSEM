import datetime

class Employee: 
    raise_amount = 1.04
    total_employees = 0

    def __init__(self,first,last,pay): 
        self.first = first  
        self.last = last
        self.email= first + '.' + last + "@co.in"
        self.pay = pay

        Employee.total_employees +=1 

    def fullname(self): 
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod # alternates the funtionality of method
    def set_raise_amt(cls, amount):  # recieves class as first argument
        cls.raise_amount = amount
    
    # classmethods as alternative constructors
    # provides alternative ways to create instances
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)
    
    # static methods don't pass in anything automatically
    # regular methods having connection with class
    # if instance or class is not accessed in the function likely static method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee("Shruti","Sen",500000)
emp_2 = Employee("Test","User",600000)

Employee.set_raise_amt(1.05)
# similar to Employee. raise_amount = 1.05
# can be called by an instance

# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)

# emp_str_1 = "Shruti-Sen-100000"
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)

my_date = datetime.date(2016,7,10)
print(Employee.is_workday(my_date))

