class NegativeAgeError(Exception):
    pass

def get_age():
    age = int(input("Enter your age: "))
    if age < 0:
        raise NegativeAgeError("Age cannot be negative.")
    return age

try:
    age = get_age()
    print("Your age is:", age)
except NegativeAgeError as e:
    print("Error:", e)
