# map function

# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))


list1 = [30, 40, 70, 90]
list2 = [10,20, 70, 40]

print(list(map(lambda x,y : x+y, list1, list2)))

# filter

list_names = ['chandler', 'joey', 'phoebe', 'monica', 'r', 'a', 'yu']
print(list(filter(lambda name : True if len(name) >=3 else False, list_names)))

# reduce

from functools import reduce

print(reduce(lambda x,y: x*y, [3,4,5, 10,2]))





