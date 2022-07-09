# copyright 2022 Jalloh, Zainab

class Comics:
    # doesn't include exception default values
    def __init__(self, **kwargs):
        if 'pub' in kwargs: self._pub = kwargs['pub']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'title' in kwargs: self._title = kwargs['title']

# uses a try/catch block to catch if there is actually a value. If none, instead of default params it returns None
    def pub(self, p=None):
        if p: self._pub = p
        try: return self._pub
        except AttributeError: return None

    def name(self, n=None):
        if n: self._name = n
        try: return self._name
        except AttributeError: return None

    def title(self, t=None):
        if t: self._title = t
        try: return self._title
        except AttributeError: return None

    def __str__(self):
        return f'The heor is {self.name()}, a character in {self.title()} published by {self.pub()}.'

class Mutants(Comics):
    def __init__(self, **kwargs):
        self._name = 'Storm'
        if 'name' in kwargs: del kwargs['name']
        super().__init__(**kwargs)

class Aliens(Comics):
    def __init__(self, **kwargs):
        self._name = 'Thor'
        if 'name' in kwargs: del kwargs['name']
        super().__init__(**kwargs)

def main():
    c1 = Mutants(name ='Storm', title = 'X-Men')
    c2 = Aliens(name = 'Superman', title='Justice League')
    print(c1)
    print(c2)

if __name__ == '__main__': main()
