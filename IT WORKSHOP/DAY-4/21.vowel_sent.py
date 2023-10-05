s = input("Enter a sentence: ")
count = 0
i = 0
for i in range(len(s)):
    if (s[i] in "AEIOUaeiou"):
        count += 1

print("Number of vowels in the given string is: ", count)