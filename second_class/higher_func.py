from functools import reduce
# map, filter and reduce function
# they're paradigms of functional programming that allow devs to itereate through an iterable and carry out an operation on each item in the iterable
# map function
name_list = ['henry', 'james', 'john', 'sandra', 'francis']
upper_name = map(str.upper, name_list)
print(list(upper_name))

numbers = [2, 4, 6, 7, 8, 23, 43, 63, 32, 90]

# def sqt_num(num):
#     return num * num

# num_list = [num * num for num in numbers]

# result = list(map(sqt_num, numbers))
# print(result)

# filter function
def is_a_student(score):
    return score > 10

num_list = [num * num for num in numbers]
a_grades = list(filter(is_a_student, num_list))
print(a_grades)

scores = [20, '30', '12', 90, '40', '26', 9, 31, 'two', 'five', 5]

def is_number_only(num):
    return isinstance(num, int)

reslt = list(filter(is_number_only, scores))
print(reslt)

def is_letter_only(strng):
    return isinstance(strng, str) # isinstance is a built-in python method 

res = list(filter(is_letter_only, scores))
print(res)

# reduce function 
# examples 
# def addition(a, b):
#     return a + b

# red = reduce(addition, numbers)
# print(red)

