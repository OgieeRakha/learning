empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7 ]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits = list("432985617")
print(digits)

more_numbers = list(numbers)
more_numbers_1 = numbers [:]
more_numbers_2 = numbers.copy()
print(more_numbers)
print(more_numbers_1)
print(more_numbers_2)
print(numbers is more_numbers)
print(more_numbers is more_numbers_1)
print(more_numbers_1 is more_numbers_2)
print(more_numbers == more_numbers_1)