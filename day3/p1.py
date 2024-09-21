words = input('Enter few sweets(space seperated): ').split()
words_tuple = tuple(words)
print(f'Words : {words}')
print(f'Words : {words_tuple}')

with open('sweets.txt', 'w') as sweets_file:
    sweets_file.write(f'List: {words}\n')
    sweets_file.write(f'Tuple: {words_tuple}\n')
print('Data written into the file: ')
with open('sweets.txt', 'r') as fptr:
    line_list = fptr.readline()
    line_tuple = fptr.readline()
    print(line_list)
    print(line_tuple)