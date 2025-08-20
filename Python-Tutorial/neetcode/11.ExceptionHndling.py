try:
    result = 10/0
except:
    print("An error occured!")
print("This will be printed regardless")

# Error Catching
try:
    result = 10/0
except Exception as error: # Exception can be any error
    print("Error: ",error)

# Multiple Except Blocks
try:
    num1 = int(a)
    num2=int(b)
    result = num1/num2
except ValueError:
    print("Error: Invalid value!")
except ZeroDivisionError:
    print("Error: Division by zero!")
except Exception as error: 
    print("Error: ",error)