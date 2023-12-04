# print('start running code here') # Beware of creating infinite loops!
# num = 0
# while num < 5:
#     print(num)
#     num += 1

# print('Normal code continues') 

# Guessing game
magic_num = 10 

# number = int(input('guess my jackpot number: '))
# while number != magic_num:
#     number = int(input('failed try again: 🤣'))

# print('hurray you got it 🙌')

# Break statement: To stop the iteration cycle at a particular point
i = 0
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# Continue statement: To skip a particular value and continue the iteration  
# while i < 6:
#     if i == 3:
#         continue 
#     i += 1
#     print(i)

# Exercise 
applicants = []

# while len(applicants) < 7:
#     name = input('what is your name? ')
#     applicants.append(name)
#     if len(applicants) == 6:
#         break
#     print(applicants)  

# Correction
# applicants_list = []
# while len(applicants_list) < 6:
#     name = input('what is your name?')
#     applicants_list.append(name)
#     print(applicants_list)

# print('Sorry! Application closed')

# For loops
num_list = [9,8,3,5,7,4,0,7,2,1]
# for n in num_list:
#     print(n)

# for n in num_list:
#     m = n + 2 
#     print(m)

# for x in range(10):
#     print(x * 1)

# fruits = ['apple', 'orange', 'banana']
# for f in fruits:
#     print(f.upper())
# notice that dot(.) notation is used with string methods!

number_list = [4,7,8,9,4,6,3,6,3,6,2]
even_list = []
for num in number_list:
    if num % 2 == 0:
        even_list.append(num)
print(even_list)

odd_list = []
for num in number_list:
    if num % 2 != 0:
        odd_list.append(num)
print(odd_list)

numb = set(even_list)
print(numb)
print(list(numb))