# Classes - easy to logically group data and function 
# easy to reuse and build upon
# data- attribute and function- method

# creation
class Employee: # class
    # pass
    def __init__(self,first,last,pay,message): # same as constructor; self - instance; 1st argument -self
        self.first = first # not need to manually create it 
        self.last = last
        self.email= first + '.' + last + "@co.in"
        self.pay = pay
        self._overpay = pay # protected attribute
        self.__message = message # private attribute

    def fullname(self): # by default public method
        return '{} {}'.format(self.first, self.last)

    def _calculate_overtime(self): # protected method
        return self.pay*0.02
    
    def __log_message(self): # Private method
        return(f"LOG: {self.__message}")
        

emp_1 = Employee("Shruti","Sen",500000,"My account") # instance of class, gets passed automatically
emp_2 = Employee("Test","User",600000,"My account")
print(emp_1)
print(emp_2)
print(emp_1._calculate_overtime()) # can be still access but is bad practice
print(emp_1._Employee__log_message()) # can still be accessed via mangeled name for debugging purposes only

# emp_1.first = "Shruti" # instance variable - unique to its instance
# emp_1.last ="Sen"
# emp_1.email = "abc@co.in"
# emp_1.pay = 2000000

# emp_2.first = "Test"
# emp_2.last ="User"
# emp_2.email = "xyz@co.in"
# emp_2.pay = 1000000

print(emp_1.email)
print(emp_2.email)

# print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_1.fullname()) # use () to get the method value
print(Employee.fullname(emp_1)) # when calling class also call the instance

