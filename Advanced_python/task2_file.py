# File Handling
# write file

file = open('test.txt', 'a')
file.write('This is a test file again')
file.close()

# Read file

file = open('test2.txt', 'r')
content = file.readlines()
print(content)
file.close()

# Append file

f = open("test2.txt", "a")
f.write("\n This is append.")
f.close()

#open and read the file after the appending

f = open("test2.txt", "r")
print(f.read())

# Delete file

import os
os.remove("test3.txt")
