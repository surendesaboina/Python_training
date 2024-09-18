numbers = [1,2,4,2,10,9,1,2,1,4,7,6,8,8,8,10,0]

unique_numbers = list(set(numbers))

numbers_dic = {}

for i in range(len(unique_numbers)):
    repeated = numbers.count(unique_numbers[i])
    numbers_dic[unique_numbers[i]] = repeated

print(numbers_dic)