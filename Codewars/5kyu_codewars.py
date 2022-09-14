# 5 kyu Where my anagrams at?

def anagrams(word, words):
    return [i for i in words if set(i) == set(word) and len(i) == len(word)]
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))

# 5 kyu Scramblies

def scramble(s1, s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True

print(scramble('rkqodlw', 'world'))
print(scramble('qmuoehmas','memosha'))
print(scramble('katas', 'steak'))

# 5 kyu Moving Zeros To The End
def move_zeros(lst):

    return sorted(lst, key=lambda x: x==0 and type(x) is not bool)

print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))

# 5 kyu Best travel

import itertools

def choose_best_sum(t,k,ls):
    combos=list(itertools.combinations(ls,k))
    sums=[sum(i) for i in combos]
    sums2=[i for i in sums if i<=t]#only the sums we care about
    if sums2==[]:
        largest=None
    else:
        largest=max([i for i in sums if i<=t])
    return largest

xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print(choose_best_sum(430,8,xs))

ys = [91, 74, 73, 85, 73, 81, 87]
print(choose_best_sum(230, 3, ys))

# 5 kyu First non-repeating character

def first_non_repeating_letter(string):
    reps = [c for c in string if string.lower().count(c.lower()) == 1]
    return reps[0] if len(reps) > 0 else ""

print(first_non_repeating_letter('stress'))
print(first_non_repeating_letter('memosha'))


# 5 kyu Sum of pairs

def sum_pairs(ints, s):
    myset = set()
    for num in ints:
          required = s - num
          if required in myset:
              return [required, num]
          myset.add(num)

print(sum_pairs([11, 3, 7, 5],10))