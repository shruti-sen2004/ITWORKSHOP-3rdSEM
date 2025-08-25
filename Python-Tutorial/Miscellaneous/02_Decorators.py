## closure - remembers message variable even after the outer function is done executing
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

hi_func = outer_function("Hi")
bye_func = outer_function("Bye")
hi_func()
bye_func()

## Decorator - func that takes another func as argument adds functionality 
## and and returns another function without altering the source code of the 
## original func
## both classes and methods can be used as decorators 
## preserve the info of original method - func module and wrapper class -> can use stacked decorator

def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print(f"wrapper executed this before {original_function.__name__}")
        return original_function(*args, **kwargs) # variable no. of arbritrary and keyword arguments (can be called anything)
    return wrapper_function

class decorator_class(object):
    def __init__(self,original_function):
        self.original_function = original_function

    def __call__(self,*args, **kwargs):
        print(f"wrapper executed this before {self.original_function.__name__}")
        self.original_function(*args, **kwargs)
        
@decorator_function
def display():
    print("Display function ran")

@decorator_function
def display_info(name, age):
    print(f"Arguments passed are ({name},{age})")

# decorator_display = decorator_function(display) # similar to @display_function
# decorator_display()
display_info('Shruti','21')
display()