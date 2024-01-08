# PYTHON CONDITIONS AND IF STATEMENTS
# python supports the usual logical conditions from mathematics
# equals: a == b
# not equals: a != b
# less than: a < b
# less than or equal to: a <= b
# greater than: a > b
# greater than or equal to: a >= b    

# PS: these conditions can be used in several ways, most commonly in "if statements" and loops
# an "if statement" is written by using the "if" keyword

# e.g 
a = 33
b = 200
if b > a:
    print('b is greater than a')

# PS: python relies on indentation to define the scope in the code, other programming languages like JavaScript oft use curly brackets "{}"
# NB: an if statement without indentation will throw an error 

# ELIF
# the elif keyword is python's way of saying "if the previous conditions were false, then try this condition"
# e.g
a = 33
b = 33
if b > a: 
    print('b is greater than a')
elif a == b: 
    print('a and b are equal')

# ELSE
# the else keyword "catches" what wasn't caught by the preceding conditions 
a = 200
b = 33
if b > a: 
    print('b is greater than a')
elif a == b:
    print('a and b are equal')
else:
    print('a is greater than b')

# PS: you can also have an "else" without the "elif";
if b > a: 
    print('b is greater than a')
else:
    print('b is not greater than a')

# Ternary Operators in Python
# SHORT HAND IF 
# NB: if you have only one statement to execute, you can put it on the same line as the "if statement"
# e.g one line if statement;
if a > b: print('a is greater than b')

# SHORT HAND IF...ELSE 
# likewise, if you have only one statement to execute, one for if and one for else, you can put it all on the same line
# e.g one line if ~ else statement
a = 2 
b = 330
print('A') if a > b else print('B')
                                                                            
# PS: you can also have multiple else statements on the same line 
# e.g 
a = 330
b = 330
print('A') if a > b else print('=') if a == b else print('B')

# the "and" keyword is a logical operator and it is used to combine conditional statements
a = 200
b = 33 
c = 500
if a > b and c > a:
    print('both conditions are True')

# OR: the "or" operator is also a logical operator and it is used to combine conditional statements
# e.g test if a is greater than b OR if a is greater than c
if a > b or a > c:
    print('At least one of the conditions is true')

# NOT: the "not" keyword is another logical operator and it is used to reverse the result of the conditional statement
# e.g test if a is NOT greater than b
a = 33
b = 200
if a > b:
    print('a is NOT greater than b') 

# NESTED IF
# you can have "if" statements inside if statements, a.k.a nested "if" statements  
# e.g 
x = 41
if x > 10:
    print('above ten')
    if x > 20:
        print('and also above 20!')
    else:
        print('but not above 20')
        
# THE PASS STATEMENT 
# if statements "cannot" be empty, but if you for some reason have an if statement with no content, put in the "pass" statement to avoid an error
# e.g 
if b > a:
    pass

