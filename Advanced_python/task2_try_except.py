# try except
try:
  print(x)
except:
  print("An exception occurred")

# else
try:
  print("Hello")
except:
  print("Bye")
else:
  print("Okay bye!")

# finally

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

try:
 a = 10
 b = 2/a
 x = 0
 file = open('test.txt', 'r')
 file.read()
 print(x)
 print('Try block executed successfully')
except ZeroDivisionError:
 print("got into except for divide by zero")
 b =0
 print(b)
except IOError:
 print('file used incorrectly')
except Exception as err:
 print(err.args)
 print('this is a generalized except block')
else:
 print('no exceptions')
 print(b)
finally:
 print('This gets executed anyhow')
