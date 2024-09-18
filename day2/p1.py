# ind the sum of the numbers passed via the command line

import sys
numbers = sys.argv
sum = 0
for i in range(1,len(numbers)):
    sum += int(numbers[i])
print(f'Sum is {sum}')