# an iterator is an object which contains a countable number of values which can be iterated upon!
# it is also an object which implements the the iterator protocol which consists of methods "__iter__()" and "__next__()"
# examples of iterables: lists, tuples, dictionaries and sets | use dir() to determine whether an object is iterable or not
# NB: They are "iterable containers" from which you can get "iterators" from!
# all these objects have an "iter()" method which is used to get an iterator

#e.g
numbers = [2, 4, 6, 7, 9, 1]
print(dir(numbers))

numbers = iter(numbers)

print(type(numbers))

print(next(numbers))
print(next(numbers))

fruits = ['apple', 'watermelon', 'banana']
fruits = iter(fruits)

print(next(fruits))
print(next(fruits))
print(next(fruits))

# NB: Even strings are iterable objects and can return an iterator
tribesman = 'PDamz'
tribesman = iter(tribesman)

print(next(tribesman))
print(next(tribesman))
print(next(tribesman))
print(next(tribesman))
print(next(tribesman))

# looping through an iterator: NB: you can also use 'for' loop to iterate through an iterable object
# e.g iterate the values of n in a tuple 
mytuple = ('apple', 'watermelon', 'banana')

for x in mytuple:
    print(x)

# e.g
myChurch = 'powerpointtribe'

for n in myChurch:
    print(n)
# the 'for' loop actually creates an iterator object and executes the next() method for each loop!

# creating an iterator
# to create an object/class as an iterator, you have to implement the methods '__iter__()' and '__next__()' to your object
# NB: all classes have the '__init__()' function; this allows you to do some initialization when the object is being created
# the '__iter__()' works in a similar fashion i.e you can do operations (initializing etc) but you must always return the itself
# the '__next__()'   ''    ''   ''    ''          ''    ''    ''            ''               ''   ''     ''     ''   ''  ''

# example: create an iterator that returns numbers, starting with 1 and each sequence will increase by one (returning 1,2,3,4,5 etc.)
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
# the example above would continue forever if you had enough next() statements or if it was used in a 'for' loop
# to prevent the iteration from going on forever, we can use the 'StopIteration' statement
# in the '__next__()' method, we can add a terminating condition to raise an error if the iteration is done a specified number of times

# e.g to stop the iteration after 20 iterations
class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration 

myclas = MyNumber()
myiter = iter(myclas)

for x in myiter:
    print(x)






# making an object iterable

class SquareTwo:
    def __init__(self, max = 0):
        self.index = 0
        self.max = max

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index > self.max:
            raise StopIteration
        
        result = 2 ** self.index
        self.index += 1 
        return result
    
# python generators 
# a generator is a special type of function which does not return a single value, rather it returns an iterator object with a sequence of values.
# NB: in a generator function, a 'yield' statement is used rather than a return statement 
# NB: generator objects are used either by calling the next method on the generator object or using the generator object in a 'for in' loop
# e.g
def PowTwoGen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

def get_seq_upto(num):
    for x in range(num):
        yield x 

# map, filter, reduce function
# these functions are paradigms of functional programming, they allow you to write simpler, shorter code without necessarily needing to bother about intricacies like loops
# map() function
# it passes each element in the iterable through the function and returns the result of all elements having passed through the function

# map(func, *iterables)
# the function returns a map object which is a generator object, to get the list result, we apply the list()
# e.g of map
my_pets = ['alfred', 'tabitha', 'william', 'ariel']
uppered_pets = list(map(str.upper, my_pets))
print(uppered_pets)

# ex 2
circle_areas = [3.56773, 5.5766, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1, 7)))
print(result)
# the range(1, 7) function acts as the second argument to the round function(the number of required decimal places per iteration) 
# NB: revise this example again 

# filter() function 
# filter() requires the function to return boolean values (true or false) and then passes each element in the iterable through the function "filtering" away those that are false
# syntax: filter(func, iterable)

# e.g
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score > 75

over_75 = list(filter(is_A_student, scores))
print(over_75)

# palindrome example 
dromes = ['demigod', 'rewire', 'madam', 'freer', 'nursesrun', 'anutforajaroftuna', 'kiosk']
palindromes = list(filter(lambda word: word == word[::-1], dromes))
print(palindromes)

# reduce() function
# it applies a function of two arguments cumulatively to the elements of an iterable i.e the reduce function returns a single result which is the cumulation of the iterable
# NB: reduce takes the first and second elements in the iterable and passes them to the function respectively, the function computes their sum and returns it to reduce, reduce then takes the result and applies it as the first element to func and takes the next element (third) in iterable as the second element to func. this cycle continues(cumulatively) till the iterable is exhausted
# e.g
from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second
result = reduce(custom_sum, numbers)

print(result)

# zip function
# it returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together
# zip() combines iterables into tuples 
# syntax: zip(iterable1, iterable2)
# e.g
a = ('john', 'charles', 'mike')
b = ('jenny', 'christy', 'monica')

x = zip(a, b)
# use the tuple() function to display a readable version of the result:

print(tuple(x)) 