#  ******* PYTHON RULES ******

# QUOTES

# Single and double quotes are the same, 
# triple quotes for multiple lines
# f stands for format. It is a property of the string class

from re import S


print(f'''
    Use triple quotes to 
    print text in multiple lines
''')

print(f' use single quotes to print in a single line')

# NAMES 

# functions - lowercase & underscore(_)

def my_function():
    print(f'Function names should be lowercase or use underscore')


# variables - Starts with alphabet or _
# Can contain number, alphabet or underscore & case sensitive
# Cannot have special chars. or start with a number
x = 2
bark = 'a dog barking!'
_meow = 'a cat meows!'
Python_Naming_Guide = 'https://pythonguides.com/python-naming-conventions/'

print(bark)
print(_meow)
print(Python_Naming_Guide)

# method - lowercase, separate multiple words with underscore
# non-public method names should start with underscore(_)
# mangle method name using two underscores __

_title = 'juNot diAz. The string tiTle metHOd title cases a string'
title_method = _title.title()
print(title_method)

# mangle a method name is like making it private to its class
# mangled variables cannot be accessed/modified outside of the class
# except by appending the parent class first then the mangled variable

class Student:
    def __init__(self, name):
        self.__name = name

s1 = Student('Fatima')
# print(s1.__name)  --> Will not print, name not accessible outside of the class
print(dir(s1))
print(s1._Student__name)


class Map:
    def __init__(self):
        self.__geek()
    
    def geek(self):
        print('In parent class')

    # private copy of original geek() method
    __geek = geek

class MapSubClass(Map):
    # provides new signature for geek() but
    # does not break __init__()

    def geek(self):
        print('In Child Class')


# Driver's code, accesses the geek method is parent.
obj = MapSubClass()
obj.geek()

# Constructor __init__() method initializes the obj state.
# initializes the (assigned values) to data members of class when object of the class is created. 
# 

class Person():

    hair_color = 'My hair is brown'
    eye_color = 'My eyes are brown'

    # init/contructor method
    def __init__(self, name):
        self.name = name
        print(self.hair_color)

    def say_hi(self):
        print('Hello, my name is', self.name)
        print(self.eye_color)


# p1 is an object of the Person class
# The Isata argument is passed to the __init__ method to initialize the object
# the keyword self reps. instance of the class and binds the attributes of Person to the argument, Isata
p1 = Person('Isata')
p1.say_hi() 


# Arguments - passable parameters

# *args - non-keyword argumensts --> passes variable number or arguments to a function
# **kwargs - keyword arguments -- passes keyworded variable-length argument list

# *args
def the_args(self, *args):
    print('the self arg is first')
    print(self)
    for arg in args:
        print(arg)
   
the_args('These are my favorite authors:', 'Oscar Wilde', 'Octavia Butler', 'Tamora Pierce')

def _the_kwargs(self, **kwargs):
    print('prints keyword: argument value')
    print(self)

    for key, value in kwargs.items():
        print('%s == %s' % (key, value))

_the_kwargs('AUTHORS:', first= 'Oscar Wilde', second='Octavia Butler', third='James Baldwin')

#__name___ is a special var that return the name of the module, useful for imports
# =='__main__' string literal

#Python doesn't support forward declarations.

#when you assign a mutable, you're assigning reference to it.
#functions work the same way.
