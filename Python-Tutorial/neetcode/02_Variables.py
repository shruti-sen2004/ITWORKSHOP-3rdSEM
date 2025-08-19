capital_of_uk = "London" # snake-case commonly used in python
print(capital_of_uk)

msg = "Fist message"
msg = "Second message" # can be reasssigned
print(msg) # prints the latest assigned value

ms1, ms2 = 5,6  # multiple assignment in single line
ms1,ms2 = ms2,ms1 #swapping without third variable

# Types of Variables
print(type(12)) # int
print(type(3.5)) # float
print(type(True)) # bool 
print(type("Shruti")) # str
print(type([1,2,3])) # lst

# Dynamic typing - single variable can hold different types - determined at runtime
# C++ - statically typed but python - dynamically typed
# should be avoided in production
# dynamic - flexible, error prone
# static - safer, less flexible
variable = 10
variable = "HELLO" 

#Type Casting
print(int(3.14)) # prints 3

# Empty Variable - None
# Depicts absence of a value
var = None
print(type(var))

