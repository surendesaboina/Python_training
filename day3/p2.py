from functools import reduce

numbers = [1, 2, 3, 5, 7, 11, 19, 17, 13]

squared_numbers = list(map(lambda num: num**2, numbers))

small_numbers = list(filter(lambda num: num < 10, numbers))

numbers_sum = reduce(lambda s, num: s + num, numbers, 0)

print(f'Squared Numbers = {squared_numbers}')
print(f'Single Digit Numbers = {small_numbers}')
print(f'Sum of Numbers = {numbers_sum}')