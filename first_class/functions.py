# a function is a block of code which only runs when it is called!
# you can pass data a.k.a parameters into a function 
# a function can also return data as a result

# creating a function 
def my_function():
    print('hello from a function')

# calling a function 
# to call a function, use the function name followed by parenthesis;
def my_function():
    print('hello from a function')

my_function()

# ARGUMENTS
# information can be passed into functions as arguments
# arguments are specified after the function name, inside the parameters. you can add as many arguments as you desire just separate them with a comma
# the following example has a function with one argument (fname). when the function is called, we pass along a first name which is used inside the function to print the full name 
# e.g 
def my_function(fname):
    print(fname + " Refsnes")

my_function('Emil')
my_function('Tobias')
my_function('Linus')

# PS: arguments are often shortened to args in python documentation
# PPS: arguments and parameters are oft used interchangeably but....from a function's perspective;
# a "parameter" is the variable listed inside the parenthesis in the function definition while
# an "argument" is the value that is sent to the function when it is called 

# Number of Arguments
# NB: by default, a function must be called with the correct number of arguments
# e.g 
def my_function(fname, lname):
    print(fname + " " + lname)

my_function('iniubong', 'isemin')
# PS: if you try to call the function with 1 or more than 2 arguments, you will get an error

# ARBITRARY ARGUMENTS
# if you don't know how many arguments are to be passed into your function, add a "*" before the parameter name in the function definition 
# NB: this way, the function will receive a tuple of arguments and can access the items accordingly 
# e.g 
def my_function(*kids):
    print('the youngest child is ' + kids[2])

my_function('Utom', 'Utty', 'Ini')
# PS: arbitrary aruments are often shortened to "args" in python documentations

# KEYWORD ARGUMENTS
# you can also send arguments with the "key = value" syntax 
# this way the order of the arguments does not matter ;)
def my_function(child3, child2, child1):
    print('the youngest child is ' + child3)

my_function(child1 = "Utom", child2 = 'Utty', child3 = 'Ini') 

# the phrase "keyword arguments"  are often shortened to "kwargs" in python documentations

# ARBITRARY KEYWORD ARGUMENTS
# if you do not know how many keyword arguments that will be passed into your function, add two asterisks "**" before the parameter name in the function definition
# this way the function will receive a dictionary of arguments and can access the items accordingly
# e.g 
def my_function(**kid):
    print('His last name is ' + kid["lname"])

my_function(fname = 'Iniubong', lname = 'Isemin')

# PS: arbitrary keywords are often shortened to **kwargs in python documentations

# DEFAULT PARAMETER VALUE
# the following example shows how to use a default parameter value
# NB: if we call a function without an argument, it uses the default parameter value

def my_function(country = 'Nigeria'):
    print('I am from ' + country)

my_function('Sweden')
my_function()
my_function('South Africa')
my_function('Seychelles')

# PASSING A LIST AS AN ARGUMENT
# you can send any data type of argument to a function (string, number, list, dictionary etc.) and it will be treated as the same data type inside the function
# e.g if you send a List an argument, it will still be a List when it reaches the function
def my_function(food):
    for x in food:
        print(x)

fruits = [ 'apple', 'banana', 'cherry' ]   
my_function(fruits)

# RETURN VALUES
# to let a function return a value, use the "return" statement
# e.g 
def my_function(x):
    return 5 * x 

print(my_function(3))
print(my_function(5))
print(my_function(8))

# POSITIONAL-ONLY ARGUMENTS
# you can specify that a function can have ONLY positional arguments, or ONLY keyword arguments
# to do this, add ", /" after the arguments
# e.g 
def my_function(x, /):
    print(x)

my_function(3)
# NB: without the ", /" after the arguments, you can still use keyword arguments even if the function expects positional arguments
# e.g 
def my_function(x):
    print(x)

my_function(x = 3)
# PS: if you add the ", /" and call the function with a keyword argument, you will get an error

# KEYWORD-ONLY ARGUMENTS
# to specify keyword-only arguments, add *, before the arguments!
# e.g 
def my_function(*, x):
    print(x)

my_function(x = 3)
# PS: without the "*," you are allowed to use positional arguments even if the function expects keyword arguments
# e.g 
def my_function(x):
    print(x)

my_function(3)
# PS: when you add the "*, /" you'll get an error if you try to send a positional argument

# COMBINING POSITION ONLY AND KEYWORD ONLY 
# you can combine the two arguments types in the same function 
# any arguments BEFORE the "/ ," are positional-only and any arguments after the "*," are keyword-only 
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(3, 6, c = 5, d = 8)

# RECURSION
# python also accepts function recursion which means a defined function can call itself 
# recursion is a common mathematical and programming concept i.e it means that a function can call itself. you can use it to loop through data to reach a desired result 
# PS: be careful with recursion as you could easily slip into writing a function which never terminates or one that uses excessive amounts of memory processing power

# e.g the function tri_recursion() is defined to "recurse", we use the "k" variable as the data which decrements(-1) every time we recurse. the recursion ends when the condition is not > 0 (i.e when it is 0)
def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6) 
