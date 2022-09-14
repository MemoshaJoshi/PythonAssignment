# loops
# while loop
i = 1
while i < 20:
  print(i)
  i += 2

# for loop
list_nums = [2,3,4]
for num in list_nums:
    if num % 2 == 0:
        print(num,'is even')
    else:
        print(num,'is odd')

# break

names = ["millie", "hannah", "chris"]
for x in names:
  print(x)
  if x == "hannah":
    break

# continue

names = ["mill", "jen", "rocky"]
for x in names:
  if x == "hannah":
    continue
  print(x)



