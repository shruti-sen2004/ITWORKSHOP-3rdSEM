name =eval(input("ENTER A LIST OF EMPLOYEE NAMES: "))
salary= eval(input("ENTER A LIST OF SALARIES: "))
if len(name)== len(salary):
    x= dict(zip(name,salary))
    print(x)
else: 
    print("ENTER EQUAL NUMBER OF EMPLOYEE NAMES AND SALARY!!")