# class = definition object = instance of that class

class Fit:
    #  variables in class = properties (py uses diff def. for properties), aka class variables
    goals = 'baddest bitch on the block'
    motivation = 'self motivated'

    # function in class = method; self = 1st argument, not a keyword, can use something else, but self is standard (ie. args in java)
    def fit(self): 
        print('Workout')
        print(self.goals)
    
    def walk(self):
        print('Steps')

# class declaration
def main():
    # variable girls an Object of class Fit.
    girls = Fit()
    girls.fit()
    girls.walk()

if __name__ == '__main__' : main()
