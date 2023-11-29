# conditional statements
# a = 20
a = 18
# a = 31
# b = 21
b = 20
# if a > b: # returns true
#     num = a - b
#     print(num)
#     print('a is greater than b')
# elif a == b:
#     num = a * b
#     print(num)
#     print('a and b are equal')
# else: # returns false
#     num = a + b 
#     print(num)
#     print('a is less b')

# Class Work
backend = []
frontend = []

age = int(input('Hi there, how old are you? '))
name = input('what is your name? ')

# if age >= 21:
#     backend.append(age)
#     print('welcome to backend cohort_6b7; agba senior dev 🙇‍♂️🙌')
# elif age >= 18 and age < 21:
#     frontend.append(age)
#     print('welcome to frontend cohort_6b7; junior dev 😁😂')
# else:
#     print('go back to programming bootcamp for dummies 😂💔')

if age >= 21:
    print(f'congratulations {name}, you are eligible for backend web development @ univelcity; agba senior dev 🙇‍♂️🙌')
    print(age)
    backend.append(name)
    print(backend)
elif age >= 18 and age < 21:
    print(f'Hi {name} you are only elgible for frontend web development @ univelcity; agba junior dev 😁😂')
    print(age)
    frontend.append(name)
    print(frontend)
else:
    print(f'oops sorry {name} you are not eligible for any course at univelcity; go back to programming bootcamp for dummies 😂💔')
    print(age)
