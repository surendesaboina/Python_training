# Accept a number from the user and check if it is a Perfect square

import math

num = int(input("Enther the number to check if it is a Perfect square:"))
sq_root = math.sqrt(num)
f_num = math.floor(sq_root)
l_num = f_num ** 2
if l_num == num:
    print(str(num) + "is a Perfect square")
else:
    print(str(num) + "is not a Perfect square")