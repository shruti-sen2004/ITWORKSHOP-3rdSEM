age = int(input("ENTER YOUR AGE: "))

try:
    if age>=0:
        print(f"YOUR ARE {age} year(s) old")
    else:
        raise ValueError("AGE CANNOT BE NEGATIVE!")

except ValueError as e:
    print(e)
