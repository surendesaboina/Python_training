# Print second biggest digit in a number

num = int(input("Enter the number:"))

temp = num
largest_num = 0
second_largest_num = 0
while temp != 0:
    digit = temp % 10
    if digit > largest_num:
        second_largest_num = largest_num
        largest_num = digit
    elif digit > second_largest_num:
        second_largest_num = digit
    temp = temp // 10
print(f'The second largest digit in {num} is {second_largest_num}')