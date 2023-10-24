is_divisible_by_5_and_7 = lambda x: x % 5 == 0 and x % 7 == 0


start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))


divisible_numbers = []
for number in range(start_range, end_range + 1):
    if is_divisible_by_5_and_7(number):
        divisible_numbers.append(number)


print(f"Numbers divisible by both 5 and 7 in the range {start_range} to {end_range}: {divisible_numbers}")