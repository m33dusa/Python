# Python is dynamic typing - elements type determined by itself.
# null is type None. Everything is a class in python, including built-in types.


from operator import truediv


x = 'Seven '
m = "eight {} {}".format(9, 0)

#format method has methods. POsitional arguments, defaults to ordered placement.

# specify positional arguments
orderM = "eight {1} {0}".format(9, 0)

#adjust location (tab using :>or:<)
adjustM = 'eight "{1:<9}" "{0:>5}"'.format(9, 0)

#Can fill in spaces with adjust w/ something like 0s by specifying it
fillAdjustM = 'eight "{1:<09}" "{0:>05}"'.format(9, 0)

print('x is {}'.format(x))
print('m is {}'.format(m))
print('specify the order to print values: {}'.format(orderM))
print('adjusting m location {}'.format(adjustM))
print('fill empty space from adjust with 0s: {}'.format(fillAdjustM))

#sequence types includes lists, tuples, dictionaries

#lits = mutable. 
j = [1, 2, 3, 4, 5]

#for sequence through list and assign i a value in that list. 
for i in j:
    print('i is {}'. format(i))

#tuple - like list, but immutable
k = (1, 2, 3, 4, 5)

for i in k:
    print('i in k is {}'.format(i))

#range - immutable, can make mutable by conerting it to list. 
m = range(6)

#specify range start and step
mx = range(2, 16)
my = range(2, 12, 2)

for i in m:
    print('i is a range in m: {}'.format(i))

for i in mx:
    print('i is a range in m: {}'.format(i))

for i in my:
    print('i is a range in m: {}'.format(i))

#dictionary - k-v pairs

d = {'one': 1, 'two': 2, 'three': 3}
for k, v in d.items():
    print('k: {} v: {}'.format(k, v))


#conditional assignment

fd = True
n = 'Go out, the weather is nice ' if fd else 'Stay indoors'
print(n)
