#  Print the Math table of a number for upto multiples of 20

num = int(input("Enter the number for Math table upto multiples of 20: "))

for i in range(1,21):
        print(f'{num} X {i:2} = {i * num:3}')