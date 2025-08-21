def get_longer_word(word1: str, word2: str) -> str:
    if len(word1) >= len(word2): # len is used to find string length
        return word1
    else:
        return word2
print(get_longer_word("sample","plates"))
    
# string indexing
name = "Shruti Sen"
print(name[0]) # first char
print(name[6]) # middle char; space is a valid charecter
print(name[-1])  # last char
length = len(name)-1
print(name[length]) # last char

for i in range(len(name)): # string looping
    print(name[i],end =" ")
print()

for char in name: # string looping short hand
    print(char, end =" ")

# string concatination
def concatenate(word1, word2):
    new_str = word1 + word2
    if len(new_str) > 10:
        return "Too long"
    return word1 + word2  # creates new string
print(concatenate("Hello, ", "World"))

# slicing
start, end = 1, 5
print(name[start:end])  # not including end
print(name[:3])  # first 3 chars from start
print(name[4:])  # upto last char

def last_n_charecters(s:str, n:int) -> str:
    if n > len(s):
        return 
    return s[-n:] # for the last n charecters
print(last_n_charecters(name,5));

print(name[::-1])  # reverse the string

# Strings - Immutable; cannot modify an existing string
# modification creates a new string rather updating th same one

receiver,sender = "Ritu", name
msg_1 = "Hello {} I am {}.\n".format(receiver,sender) 
msg_2 = f"Hello {receiver} I am {sender}.\n"
msg_3 = "Hello {1} I am {0}.\n".format(receiver,sender) 
print(msg_1,msg_2,msg_3)

print(ord("a")) # Ascii value

strings= ["ab","cd","ef"]
print(" ".join(strings)) # output: ab cd ef