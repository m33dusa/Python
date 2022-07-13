def function(n=1):
    print(n)
    return n*2

x = function(42)
function(x)

# Check if the number we pass is prime
def isprime(n):
    if n <=1:
        return False
    for x in range (2, n):
        if n % x ==0:
            return False
    else:
        return True

# Get a list of prime numbers from a range

def listprimes():
    for n in range(100):
        if isprime(n):
            print(n, end=' ', flush=True)
    print()

listprimes()
n = 5
if isprime(n):
    print(f'{n} is prime')
else:
    print(f'{n} is not prime')

# in Python functions are used as methods and objects and to breakdown 
# other functions into manageable chunks.

def main():
    showsTupple = ('Super natural', 'smallville', 'static shock', 'filmore')
    #astriks breaks down list into new lines
    shows(*showsTupple)
    
    dictionaryBooks = dict(YA = "Twilight", Romance = "R&J", Play = "Othello")
    books(**dictionaryBooks, fiction = "Sabriel", fantasy = "Eona", SciFi = "Bloodchild")

    for i in inclusive_range(25):
        print(i, '', end = '')
    print()


def shows(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('Read!')

def books(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Genre {} Book {}'.format(k, kwargs[k]))
    else:
        print('Go watch something')

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    if numargs <1:
        raise TypeError(f'expeted at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args  
    else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

    i = start
    while i<=stop:
        yield i
        i +=step  

if __name__ == '__main__' : main()
