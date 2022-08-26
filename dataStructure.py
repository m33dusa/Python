#Lists, tuples and dictionaries

#list - mutable, Use insert, remove, pop, delete, slice, etc 
x = [1, 2, 3, 4]

#tutple - immutable
y = (1, 2, 3, 4)

#Dictionary - key, value paris.  Can use dictionary constructor.
z = {"a": 1, "b": 2, "c":3, "d":4}

#set - unordered list of unique values
a = {1, 2, 3, 4}

def main():
    #list
    genres = ["fiction", "scifi", "fantasy"]
    print(genres[1])
    genres.insert(2, "Graphic Novels")
    genres.insert(0, "YA")
    print_list(genres)
    print(", ".join(genres))

    seq = range(12)
    seq2 = (x * 2 for x in seq)
    seq3 = (x for x in seq if x%3 !=0)
    seq4 = ((x,x**2) for x in seq)
    seqDict = {x: x**2 for x in seq}
    seqSet = { x for x in "bannanas" if x not in "an"}
    print_list(seq)
    print_list(seq2)
    print_list(seq3)
    print_list(seq4)
    print(f'{seqDict}')
    print(f'{seqSet}')

    #dictionary constructor
    colors = dict(danger="red", warning="yellow", calm="blue", new="green")
    print_colors(colors)

    #mixed structures
    mx = [1, 'two', 3, {'4': 'four'}]
    my = {'one', 'two', None, 'three', 4}
    mz = set('I guess this can be fun, I mean like whatever')
    mzz = dict(one = mx, two=my, three=mz)
    mixed = [mx, my, mz, mzz]
    display(mixed)

def display(n):
    global dlevel

    dlevel += 1
    if isinstance(n, list): print_mixed(n)
    elif isinstance(n, range): print_mixed(n)
    elif isinstance(n, tuple): print_mixed(n)
    elif isinstance(n, set): print_mixed(n)
    elif isinstance(n, dict): print_mixed(n)
    elif n is None: print('None', end=' ', flush=True)
    dlevel -=1

    if dlevel <=1: print() #newline after outer.

def print_mixed(n):
    print('[',  end=' ', flush=True)
    for x in n: display(x)
    print(']', end=' ', flush=True)

def print_colors(m):    
    for k,v in m.items():
        print(f'{k}: {v}')

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()


if __name__ == "__main__": main()
