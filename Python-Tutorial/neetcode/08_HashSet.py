from typing import List
# Sets - unordered collection; contains only unique element
# implemented with Hashsets
# searching and inserton in constant time
my_set = {1,2,3}

my_set2 = set()  # don't do {}
my_set2.add(1)
my_set2.add(2)
print(my_set2)

my_set2.remove(1)  # value not index
print(my_set2)

my_set = {"Cat", "Dog", "Mouse"}
contains_cat = "Cat" in my_set  
print(contains_cat)

def count_unique_words(words: List[str]) -> int:
    if not len(words):
        return 0
    word_set = set(words)
    return len(word_set)
print(count_unique_words(["hello", "world", "hello", "great"]))

def contains_duplicate(words: List[str]) -> bool: # checks for duplicates in a list 
    words_set = set(words)
    return len(words_set) < len(words)
print(contains_duplicate(["hello", "world", "hello", "great"]))

my_set ={i for i in range(5)}
print(my_set)