def function(n=1):
    print(n)
    return n*2

x=function(42)
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

