x = "books"

def myfunc():
  x = "magazines"
  print("I like reading " + x)

myfunc()

print("I like reading  " + x)

# global variable
def myfunc():
  global x
  x = "books"

myfunc()

print("I like reading " + x)