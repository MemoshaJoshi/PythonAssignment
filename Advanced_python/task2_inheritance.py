# inheritance

class Human:
    def __init__(self, name, age, gender):
        self.age = age
        self.name = name
        self.gender = gender

    def talk(self):
        print('bla bla')

s1 = Human(name='Ram', age= 33, gender='male')
s1.talk()