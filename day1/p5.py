# Read a number from the user and print the Lucky digit of the user where the lucky digit if found by finding the sum of digits of the given number and repeat the algorithm until single digit is arrived

num = int(input("Enter the number to find the Lucky digit: "))
sum = 0
while num != 0:
    digit = num % 10
    num = num // 10
    sum += digit
    if num == 0 and sum >9:
        num = sum
        sum = 0
print(sum)