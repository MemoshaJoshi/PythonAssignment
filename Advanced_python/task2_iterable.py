tuple_1 = ("apple", "banana", "cherry")
iterable = iter(tuple_1)

print(next(iterable))
print(next(iterable))
print(next(iterable))

# string iterable
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# looping through iterable

mystr = "apple"

for x in mystr:
  print(x)