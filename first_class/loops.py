# python has two primitive loop commands:
# 1. while loops and;
# 2. for loops

# THE WHILE LOOP
# with the while loop, we can execute a set of statements as long as a condition is true
# e.g print i as long as i is less than 6;
i = 1 
while i < 6:
    print(i)
    i += 1
# PS: always remember to increment i when using "while" loops else it will continue forever
# PPS: the while loop requires relevant variables to be ready;
# e.g you need to define an indexing variable i which we set to 1

# THE BREAK STATEMENT
# with the "break" statement, we can stop the loop even if the while condition is true
# e.g exit the loop when i is 3'
i = 1 
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1 

# THE CONTINUE STATEMENT
# with the continue statement, we can stop the current iteration and continue with the next 
# e.g continue to the next iteration if i is 3;
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# THE ELSE STATEMENT
# with the else statement, you can run a block of code once when the condition no longer holds true
# e.g print a message once the condition is false 
i = 1 
while i < 6:
    print(i)
    i += 1
else:
    print('i is no longer less than 6')

# FOR LOOPS 
# a for loop is used for iterating over a sequence (i.e a list, tuple, dictionary, set or string)
# it's less like the "for" keyword in other programming languages and works like an iterator method as found in other OOP languages
# with the "for" loop we can execute a set of statements, once for each item in a list, tuple set etc
# e.g 
# print each fruit in a fruit list;
fruits = [ 'apple', 'banana', 'cherry' ]
for x in fruits:
    print(x)

# PS: the "for" loop does not require an indexing variable to set beforehand

# LOOPING THROUGH A STRING
# NB: even strings are iterable objects, they contain a sequence of characters
# e.g loop through the letters in the word 'banana'
for x in 'banana':
    print(x)

# THE BREAK STATEMENT
# with the "break" statement, we can stop the loop before it has looped through all the items
# e.g exit the loop when x is banana
for x in fruits:
    print(x)
    if x == 'banana':
        break

# e.g exit the loop when x is 'banana' but this time the break comes before the print
for x in fruits:
    if x == 'banana':
        break
    print(x)

# THE CONTINUE STATEMENT
# with the "continue" statement, we can stop the current iteration of the loop and continue with the next
# e.g do not print banana
for x in fruits:
    if x == 'banana':
        continue
    print(x)

# THE RANGE() FUNCTION
# to loop through a set of code a SPECIFIED NUMBER OF TIMES, we can use the range() function
# the range function returns a sequence of numbers, starting from 0 by default and increments 1 (by default) and ends at a specified number
# e.g using the range() function
for x in range(6):
    print(x)
# PS: range(6) refers to the values 0 - 5 not 0 - 6
# the range() function defaults to 0 as a starting value, but it's possible to specify the starting value by adding a parameter
# e.g range(2, 6) which means values from 2 to 6 (i.e values from 2-6 which means values from 2 to 6 but not including 6!)
# using the start parameter
for x in range(2, 6):
    print(x)
# PS: the range() function defaults to increment the sequence by 1 but you can specify the increment value by adding a third parameter
# e.g increment the sequence with 3: i.e range(2, 30, 3)
for x in range(2, 30, 3):
    print(x)

# ELSE IN FOR LOOP
# the "else" keyword in a "for" loop specifies a block of code to be "executed when the loop is finished"
# e.g print all numbers from 0 - 5 and print a message when the loop has ended
for x in range(6):
    print(x)
else:
    print('finally finished!')
# PS: the else block will NOT be executed if the loop is stopped by a "break" statement
# e.g break the loop when x is 3 and see what happens with the else block
for x in range(6):
    if x == 3: break
    print(x)
else:
    print('finally finished!')

# NESTED LOOPS
# a nested loop is a loop inside a loop
# the 'inner loop' will be executed once for each iteration of the outer loop
# e.g print each adjective for every fruit
adj = [ 'red', 'big', 'tasty' ]
fruits = [ 'apple', 'banana', 'cherry' ]

for x in adj:
    for y in fruits:
        print(x, y)

# THE PASS STATEMENT
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the "pass" statement to avoid errors
# e.g 
for x in [ 0, 1, 2 ]:
    pass


