def greet_1(name: str) -> None: 
    msg = "Hello, " + name # string concatination
    print(msg)
    print()
greet_1("Shruti") # can be reused for different arguments

def greet_2(name, greeting="Good Morning"):
    message = greeting + " " + name
    print(message)
greet_2("Shruti","Hello")
greet_2("Ritu") # takes the default argument value for greeting
# def greet_2(name= "Shruti", greeting): # not allowed

