x = lambda a : a + 2
print(x(5))

# multiple arguments
x = lambda a, b : a * b
print(x(5, 10))

# Lambda functions
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))