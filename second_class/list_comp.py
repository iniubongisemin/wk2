# list comprehension 
# syntax: newList = [expression for item in iterable if condition == True] NB: the "condition" is like a filter that only accepts the items that valuate to true
# the return value is a new list...leaving the old list unchanged

# examples:
list1 = [character for character in [1, 2, 3]]

# displaying list
# print(list1)

# list2 = [i for i in range(11) if i % 2 == 0]
# print(list2)

# ex 2:
# based on a list of fruits, you want a new list, containing only the fruits with the letter 'a' in the name.
# using 'for' statement:
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
# newlist = []

# for x in fruits:
#     if 'a' in x:
#         newlist.append(x)

# print(newlist)

# using 'list comprehension'
# newlist = [x for x in fruits if 'a' in x]

# print(newlist)

# ex 3: program that only accepts items that are not apple in the list of fruits
# newlist = [x for x in fruits if x != 'apple']

# print(newlist)

# iterable: this can be any iterable object e.g list, tuple, set etc.
# using the range() function to create an iterable:
# newlist = [x for x in range(11)]

# print(newlist)

# examples with condition:
# only accept numbers lower than 5:
# newlist = [x for x in range(10) if x <= 5] 

# print(newlist)

# set the values in the new list to upper case:
# newlist = [x.capitalize() for x in fruits]
# newlist = [x.upper() for x in fruits]

# print(newlist)

# to change all the elements of newlist to one value:
# newlist = ['hello' for x in fruits]

# print(newlist)

# the expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
newlist = [x if x != 'banana' else 'orange' for x in fruits]

print(newlist)
