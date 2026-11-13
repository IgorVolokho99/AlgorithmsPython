import bisect

numbers = [1, 3, 3, 3, 5, 7, 9]

print(bisect.bisect_left(numbers, 3)) # lower_bound
print(bisect.bisect_right(numbers, 3)) # upper_bound
print(bisect.bisect(numbers, 3))
bisect.insort_left(numbers, 3)
print(numbers)
bisect.insort_right(numbers, 3)
print(numbers)
bisect.insort(numbers, 3)
print(numbers)
numbers = [1, 2, 3, 3, 3, 5, 7, 9]
print(bisect.bisect_left(numbers, 2))
print(bisect.bisect_right(numbers, 2))