class Student:
    name = 'Jessica'
    age = 24

    def print_name(self):
        print(self.name)

J = Student()
print(J.name)

J.name = 'Jess'
J.print_name()

# initializer

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Chloe", 26)

print(p1.name)
print(p1.age)

#  object methods

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Daniel", 36)
p1.myfunc()