class BelowThresholdError(Exception):
    pass

def generate_random_number():
    import random
    number = random.random()  
    return number

try:
    random_number = round(generate_random_number(),4)
    print("Random number:", random_number)

    if random_number < 0.5:
        raise BelowThresholdError("Number is below 0.5")
except BelowThresholdError as e:
    print("Error:", e)
