import random

count = 0

while True:
    if count >= 10:
        raise StopIteration("Displayed 10 numbers. Exiting...")
    
    random_number = random.randint(1, 100)
    print("Random number:", random_number)
    count += 1
