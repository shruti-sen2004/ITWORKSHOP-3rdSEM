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

# Nested functions
def outer(a,b):
    c= "c"
    def inner(): # have access to outer block
        return a+b+c
    return inner()
print(outer("a","b"))

def double(arr,val):
    def helper():
        for i,n in enumerate(arr): # modifying array works
            arr[i] *= 2
        # will only modify var in helper sope
        #val *= 2

        nonlocal val
        val *=2 # this will modify val outside helper scope
    helper()
    print(arr,val)

nums = [1,2]
val = 3
double(nums,val)