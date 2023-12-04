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
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
    
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
    
# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
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