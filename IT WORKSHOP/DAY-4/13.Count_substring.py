# Read a string from the user
string = input("Enter a string: ")

# Create an empty list to store the substrings
substrings = []

for length in range(len(string)):
    for index in range(len(string) - length):
        substrings.append(string[index:index+length+1])
# Print the list of substrings
print(substrings)
