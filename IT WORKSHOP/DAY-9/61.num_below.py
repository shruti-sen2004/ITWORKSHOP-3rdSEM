import random

num = round(random.random(),4)
try:
    if num >= 0.5:
        print("THE RANDOM NUMBER GENERATED IS: ",num)
    
    else:
        raise ValueError(f'{num} is smaller than 0.5!!')
except ValueError as e:
    print(e)
