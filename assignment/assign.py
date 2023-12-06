#1 given a dataset of string and integer write logic to separate the dataset and only return a list of the integer values using the built in functions in python.
dataset = ['python', 20, 'java', 30, 41, 29, 'c#', 'maths']

def is_int(integ):
    return isinstance(integ, int)

int_data = list(filter(is_int, dataset))
print(int_data)

#2 write simple logic to remove empty strings from a list of string 
list_string = ["Mike", " ", "Emma", "Kelly", " ", "Brad", "Bruce", " ","Henry"]
name_string = []

def empty_string(emp):
    if emp != " ":
        return emp

name_string = list(filter(empty_string, list_string))
print(name_string)

#3 write a program to check if value 200 exists in the following dictionary 
simple_dict = {'a': 100, 'b':200, 'c':300, 'd':400}
list_dict = list(simple_dict.values())
print(list_dict)

for x in list_dict:
    if x == 200:
        print(True)

# dict_list = list(simple_dict)
# print(dict_list)

#4 reasons why commenting is important when coding
#i. it helps other developers understand what your code does when working in teams
#ii. it helps you remember what your code does when you come back to it after a long time 

#5 use a range of indexes to print the third, fourth and fifth item in the list
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
    