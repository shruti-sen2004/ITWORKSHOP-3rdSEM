def temp_con(temp):
    return (18*temp/100)+32

cel= float(input("ENTER A TEMPERATURE IN CELCIUS: "))
print("TEMPERATURE IN FARENHEIT IS: ",temp_con(cel))