# functions

def add(num1, num2):
    return num1+ num2

ans = add(1,5)
print(ans)

# Arbitary arguments

def my_function(*pets):
  print("My favourite pet is " + pets[2])

my_function("Cat", "Parrot", "Dog")

# keyword arguments

def my_function(**pet):
  print("My pet's name is " + pet["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# default
def my_function(name = "Maggie"):
  print("My name is " + name)

my_function("max")
my_function("Iglu")
my_function()
my_function("Brice")