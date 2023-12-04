# list comprehension 
# 'a way of creating a new list from the values of an existing list and also implementing other logic to the values of the list'
# solve the list comprehension with normal loops later
# syntax: newList = [expression(element) for element in oldList]
students = ['john', 'mike', 'lucky', 'sam', 'harry']
# uppercase_student = [name.upper() for name in students]
uppercase_student = [name.capitalize() for name in students]
print(uppercase_student)
    
# example 2
number_list = [4,7,8,9,4,6,3,6,3,6,2]
print(dir(number_list))
is_active = True
# print(dir(is_active))
# even_list = []
# even_list = set([num for num in number_list if num % 2 == 0])
# print(even_list)
# odd_list = set([num for num in number_list if num % 2 != 0])
# print(odd_list)

# iterables and iterators 
# score = 20
# for x in score:
#     print(x) # this will always bring up an error!

# iterator_obj = iter(number_list)
# print(next(iterator_obj))
# print(next(iterator_obj))

# making an object iterable
class Power_Two:
    def __init__(self, max = 0):
        self.index = 0
        self.max = max
    
    def sample_fn(self):
        pass

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index > self.max:
            raise StopIteration
        
        result = 2 ** self.index
        self.index += 1
        return result
    
# our_own_obj = Power_Two(5)
# iterator_obj = iter(our_own_obj)
# print(next(iterator_obj))
# print(next(iterator_obj))

# python generators
# a special type of function which does not return a single value instead iterable object with a sequence of values 
# NB: a yield statement is used rather than a return statement 
# examples
# def PowerTwoGen(max = 0):
#     n = 0 #index movement
#     while n < m:
#         yield 2 ** n
#         n += 1 

# new_obj = PowerTwoGen(5)
# for a in new_obj:
#     print(a)

# def sentence_gen(text):
#     start = 0
#     words = text.split()
#     while start < len(words):
#         each_word = words[start]
#         start += 1
#         yield each_word

# text1 = sentence_gen('welcome to univel backend class')
# for i in text1:
#     print(i)

my_hobby = ('I love programming')
print(my_hobby.split())
