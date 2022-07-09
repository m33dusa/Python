#!/path to executible/that runs/this/file (#!/usr/local/bin/python
#Shebang Line comment (above) requires those first two chars. Has to come first. 
#statements per line -> null closing brackets.

from operator import truediv
import platform

#version = platform.python_version()
#indenting in Python = scoped?

print("Hello World")

def main():
    message()

def message():
    print("This is python version {}".format(platform.python_version()))

if __name__ == '__main__': main()

x=42
print("Hello, world {}".format(x))

print(f"Fellow {x}")

x=422
y=60
i=100

if(x<y):
    print('x<y: x is {} and y is {}'.format(x,y))
    print('Blocks defined by indention. This is part of the same if block')
    print('Blocks do not define scope of variables')
print('This is not part of the block b/c it is outside of the indent')

if y<i:
    print('y<i: y is {} and i is {}'.format(y,i))
