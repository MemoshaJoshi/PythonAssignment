# 6 kyu Is a number prime?

def is_prime(num):

  if num <= 0 or num == 1:
    return False
  i = 2
  while (i <= num ** 0.5 ):
    if num % i == 0:
      return False
    i += 1
  return True

print(is_prime(1))
print(is_prime(2))

# 6 kyu Find the unique number

def find_uniq(arr):

  for char in set(arr):
    if arr.count(char) == 1:
      return char

print(find_uniq([1, 1, 1, 2, 1, 1]))
print(find_uniq([ 0, 0, 0.55, 0, 0 ]))

# 6 kyu Delete occurrences of an element if it occurs more than n times

def delete_nth(order, max_e):
  new_order = []

  for n in order:
    if new_order.count(n) >= max_e:
      continue
    else:
      new_order.append(n)
  return new_order

print(delete_nth([20,37,20,21], 1), [20,37,21])

# 6 kyu Write Number in Expanded Form

def expanded_form(num):
  s = []
  i = len(str(num)) - 1
  for n in str(num):
    if n != "0":
      s.append(n + "0" * i)
    i -= 1
  return " + ".join(s)

print(expanded_form(12))

# 6 kyu Mexican Wave

def wave(people):
  if len(people) == 0:
    return []
  else:
    people = people.lower()
    the_waves = []
    for e, i in enumerate(people):
      if i == " ":
        continue
      else:
        the_waves.append(people[:e] + people[e].upper() + people[e + 1:])
    return the_waves

print(wave("memosha"))


# 6 kyu Break camelCase

def solution(s):

  return "".join([" " + c if c.isupper() else c for c in s])

print(solution("camelCasing"))
print(solution("helloWorld"))


