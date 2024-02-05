from prime import prime_or_not,prime_range

num = int(input("ENTER A NUMBER: "))
if prime_or_not(num)== True:
    print(f'\n{num} is PRIME')
else:
    print(f'\n{num} is not prime')


start= int(input("\nENTER THE STARTING RANGE: "))
end= int(input("ENTER THE ENDING RANGE: "))
print(f'PRIME NUMBERS BETWEEN {start} and {end} are: ')
prime_range(start,end)
