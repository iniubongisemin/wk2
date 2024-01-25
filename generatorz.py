# GENERATOR FUNCTIONS
# a generator is a function that returns an iterator using the "yield" keyword
# NB: if the body of a def contains yield, it automatically becomes a python generator function 

# syntax:
def function_name():

    yield #statement

# e.g create a simple generator that will yield three integers, then we will print these integers by using a for loop
# the generator function yields 1 the first time, 2 the second time and 3 the third time
def simpleGeneratorFunc():
    yield 1
    yield 2
    yield 3

# driver code to check the generator function above 
for i in simpleGeneratorFunc():
    print(i)

# GENERATOR OBJECT
# python generator functions return a generator object that is iterable, i.e can be used as iterator

    
    