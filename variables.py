# !desktop/demos/python
# Copyright 2022 Jalloh, Zainab


class Book:
    def __init__(self, **kwargs):
        self._genre = kwargs['genre'] if 'genre' in kwargs else 'Fiction'
        self._author = kwargs['author'] if 'author' in kwargs else 'Octavia Butler'
        self._rating = kwargs['rating'] if 'rating' in kwargs else 'Awesome'

    def genre(self, g=None):
        if g: self._genre = g
        return self._genre

    def author(self, a=None):
        if a: self._author = a
        return self._author

    def rating(self, r=None):
        if r: self._rating = r
        return self._rating

    def __str__(self):
        return f'Author {self.author()} writes works of "{self.genre()}" and it is "{self.rating()}". '


def main():
    b1 = Book(genre = 'Historical', author = 'Susan B. Anthony', rating ='Meh')
    b2 = Book(genre = 'Fiction', author = 'Tamora Pierce', rating='Awesome')
    print(b1)
    print(b2)

    b1.genre = 'Drame'
    print(b1.genre)

if __name__ == '__main__': main()
