# 7 kyu vowels count

def get_count(sentence):
    vowels = 'aeiou'

    vowels_count = 0
    for char in sentence:
        if char.lower() in vowels:
            vowels_count +=1
    return vowels_count

vowels = 'memosha'
print(get_count(vowels))

# 7 kyu sum of odd numbers

def row_sum_odd_numbers(n):
    start = n * (n-1) + 1
    total = 0
    for i in range(n):
        total += start
        start += 2
    return total

print(row_sum_odd_numbers(1))
print(row_sum_odd_numbers(2))
print(row_sum_odd_numbers(3))

# 7 kyu over the road

def over_the_road(address, n):

    return (n * 2) - address + 1

print(over_the_road(1,3))
print(over_the_road(3,3))
print(over_the_road(2,3))

# 7 kyu Ones and Zeros

# def binary_array_to_number(arr):
#     return int("".join([str(i) for i in arr]), 2)
#
# arr1 = [0, 0, 0, 1]
# arr2 = [0, 0, 1, 0]
# print(binary_array_to_number(arr1))
# print(binary_array_to_number(arr2))

def binary_array_to_number(arr):
    s = 0
    for digit in arr:
        s = s * 2 + digit

    return s

arr1 = [0, 0, 0, 1]
arr2 = [0, 0, 1, 0]
print(binary_array_to_number(arr1))
print(binary_array_to_number(arr2))

# 7 kyu Remove anchor from URL

def remove_url_anchor(url):

    return url[:url.find("#")] if "#" in url else url

print(remove_url_anchor('www.codewars.com#about'))
print(remove_url_anchor('www.codewars.com?page=1"'))

# 7 kyu Testing 1-2-3

def number(lines):
    count = 1
    line = []
    for x in lines:
        line.append(str(count) + ': ' + x)
        count += 1
    return line

lines = ["a", "b", "c"]
print(number(lines))



