# Data Types

x = "apple"
print(type(x))

x =4
print(type(x) is not float)
# the type of x is int here, so this line returns true value.

students = ['John','Marry',"Harry"]
print("Henry" in students)

# Type conversion

x = 5   # int
y = 1.2  # float
z = 3j-1   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))