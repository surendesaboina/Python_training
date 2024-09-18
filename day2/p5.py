my_list = [2,3,5,7,9]
print(my_list)
my_list[1::3] = (e**2 for e in my_list[1::3])
print(my_list)