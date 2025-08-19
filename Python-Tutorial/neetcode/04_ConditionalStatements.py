# if statements
# does not create a new scope like function
# if if-statement is in global scope shares global scope
# if defined inside a function only limited to scope of the function
if True: 
    message ="Hello"
print(message)
print()

# Truthy and Falsy
# non-boolean variable are used as True or False
msg_falsy = "" 
msg_truthy = "Hi!"
if msg_falsy: # "" is evaluated as False
    print("Message is empty") # is not printed
if msg_truthy:
    print("Message is not empty") # is printed