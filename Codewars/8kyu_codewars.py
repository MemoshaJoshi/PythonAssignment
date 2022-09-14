# 8 kyu 10 problems
# 8 kyu Multipy

def multiply(a, b):
    return a * b

mul = multiply(4,5)
print(mul)

# 8 kyu Reversed words

def reverse_words(s):
    # first split the string into words
    words = s.split(' ')

    # then reverse the split string list and join using space
    rev_sentence = ' '.join(reversed(words))

    # finally return the joined string
    return rev_sentence

sentence = "The greatest victory is that which requires no battle"
print(reverse_words(sentence))

# 8 kyu Grasshopper- check for factor

def check_for_factor(base, factor):
    return (base % factor == 0)

print (check_for_factor(8,2))
print (check_for_factor(3,2))

# 8 kyu Do I get a bonus?

def bonus_time(salary, bonus):
    if bonus is True:
        salary = salary * 10;

    return "$" + str(salary);

print(bonus_time(500, True))
print(bonus_time(100, False))

# 8 kyu Get Planet Name By ID

def get_planet_name(id):
    # This doesn't work; Fix it!

    name = ""
    match id:
        case 1:
            name = "Mercury"
        case 2:
            name = "Venus"
        case 3:
            name = "Earth"
        case 4:
            name = "Mars"
        case 5:
            name = "Jupiter"
        case 6:
            name = "Saturn"
        case 7:
            name = "Uranus"
        case 8:
            name = "Neptune"
    return name

print(get_planet_name(1))
print(get_planet_name(2))
print(get_planet_name(3))

# 8 kyu To square(root) or not to square(root)

import math

def square_or_square_root(arr):
    t = []
    for x in arr:
        if math.sqrt(x) == int(math.sqrt(x)):
            t.append(int(math.sqrt(x)))
        else:
            t.append(x ** 2)

    return t

sq = [4,3,9,7,2,1]
print(square_or_square_root(sq))

# 8 kyu Grasshopper - Grade book

def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) // 3
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90 :
        return "B"
    elif 70 <= score < 80 :
        return "C"
    elif 60 <= score < 70 :
        return "D"
    else:
        return "F"

print(get_grade(95, 92, 90))
print(get_grade(30, 80, 60))

# 8 kyu Grasshopper - Messi goals function

def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

print(goals(5, 10, 2))

# 8 kyu Grasshopper - Personalized Message

def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"

owner = 'Daniel'
print(greet('Daniel', owner))
print(greet('George', owner))
print(greet('Nancy', owner))

# 8 kyu Transportation on vacation

def rental_car_cost(d):
    if 3 <= d < 7:
        return (d * 40) - 20
    elif d >= 7:
        return (d * 40) - 50
    else:
        return d * 40

print(rental_car_cost(4))
print(rental_car_cost(9))

