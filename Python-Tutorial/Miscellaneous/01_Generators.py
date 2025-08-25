## iterators - objects that enables a programmer to traverse a container, particularly lists
## generator - Routine to control iterator behaviour. Similar to function that returns an array.
## use case of generator - large data traversal w/o storing. Only care about current element.
import sys 

x = [1,2,3,4,5,6,7,8,9,10] 
print(sys.getsizeof(x))
print(sys.getsizeof(range(1,11))) # iterator -range, smaller in size than x

y = map(lambda i: i**2, x) # iterate through values w/o storing them

## next() or __next__()
## for loop calls next() on the iterated object
print(next(y)) # returns the next value in sequence 
print(next(y)) 
print(y.__next__())

## iter() or __iter__()
## to iterate : iter() -> Next()
x = range(1,11)
print(next(iter(x)))

## creating legacy iterators
class Iter:
    def __init__(self,n):
        self.n =n
    
    def __iter__(self):
        self.current = -1
        return self
    
    def __next__(self):
        self.current +=1

        if self.current >= self.n:
            raise StopIteration
        return self.current

x = Iter(5)
for i in x:
    print(i)

# print(next(x)) # gives error
itr = iter(x)
print(next(x))

## Creating generator 
def gen(n): # auto-implements iter and next for us
    for i in range(n):
        yield i # pauses executuion untill we see the next keyword again

for i in gen(5):
    print(i)

## Generator comprehension
x = (i for i in range(10))
print(x)
print(next(x))
for j in x:
    print(j)