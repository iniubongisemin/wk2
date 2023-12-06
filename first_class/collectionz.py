# Set collections examples 
# "A collection of unordered items" Feat: Unique, Immutable, Zero duplicates, Unindexed, Curly braces
# NB: Items can be added and removed from the set

# Methods: add(), update(), remove(), discard()
list()
tuple()
set()

new_student = 'badmus'
new_student = set()
# print(new_student) 
# print(type(new_student)) 

student_set = {'mike', 'john', 'mike', 'john'}
student_set.add('harry')
# print(student_set)

student_set.remove('john')
# print(student_set) 

new_student.add('sandra')  
new_student.add('joy')
new_student.add('emeka')
# print(new_student) 
# print(type(new_student)) 

all_student = {'inie','success','marvellous','badmus'} 
# print(type(all_student))

# print('before update:', student_set)  

student_set.update(new_student)
# print(new_student) 
# print('after update:', student_set)

people = {'henry', 'john'}
people.add('daxit')
# print(people)

# Union Operation on Sets
# Two sets can be merged using union() function or | operator
xmen = {'xavier', 'magneto'}
droids = {'daniel', 'doberman'}

population = people.union(xmen)
hoomans = people | xmen
# print(hoomans)
# print(population)

citizens = people | droids
# print(citizens)

# Intersection Operation on Sets
# This can be done through intersection() or & Operator
set1 = {1, 3, 5, 7, 8}
set2 = {1, 5, 3, 6, 8, 9}
set3 = set1.intersection(set2)
set4 = set1 & set2
# print(set3)
# print(set4)

this_set = {'apple', 'banana', 'cherry'}
# Looping with for-loop
# for x in this_set:
#     print(x)

this_set = {'apple', 'banana', 'cherry'}
x = this_set.pop() # to remove a random element
# print(this_set)

this_set.remove('banana')
# print(this_set)

fruits = {'apple', 'orange', 'tangerine'}
faang = {'facebook', 'apple', 'amazon', 'netflix', 'google'}

fruits.update(faang) # insert the items from set faang into set fruits
# print(fruits)

# Operators for Sets
# Operator      |  Notes
# key in s      |  containment check
# key not in s  |  non-containment check
# s1 == s2      |  s1 is equivalent to s2
# s1 != s2      |  s1 is not equivalent to s2
# s1 <= s2      |  s1 is a subset of s
# s1 < s2       |  s1 is a proper subset of s2
# s1 >= s2      |  s1 is a super subset of s2
# s1 > s2       |  s1 is a proper superset of s2
# s1 | s2       |  union of s1 and s2 
# s1 & s2       |  intersection of s1 and s2 
# s1 - s2       |  the set of elements in s1 that are not in s2  

# Dictionary
# A collection of data stored in key-value pairs which are ordered, changeable and do not allow duplicates
# values may be of any datatype but keys must be of an immutable datatype e.g strings, numbers or tuples 
my_details = {
    'name': 'inie',
    'age':  '2x',
    'email':'eugeneinie@outlook.com',
    'address':{
        'no': 38,
        'street':'moleye',
        'town':'yaba',
        'state':'lagos', 
        'country':'nigeria'
    },
    'colors':['blue','black','red']
} 

# print(my_details['name'])
# print(my_details['age'])
# print(my_details['address']['state'])

my_details['height'] = '5ft 8inches'  # sets a new key-value pair in the dict
# print(my_details)

photocopy = my_details.copy()
# print('original: ', my_details)
# print('photocopy: ', photocopy)
# print(my_details.keys())
# print(my_details.pop('height'))
my_details.update({'email': 'iceley007@gmail.com'}) # when updating keys, the key and its value are nested in curly braces 
# print('update: ', my_details)

my_details.setdefault('height', 1.78) # sets a new key value pair in the dict but not if there's already a key-value pair with the same details
print('update: ', my_details)
