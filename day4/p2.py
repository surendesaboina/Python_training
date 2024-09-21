try:
    suren = print('Suren') # print() returns nothing
    print(suren) #None
    print(len(suren)) # causes exception
except TypeError as exp:
    print('Some Error Occured')
    print(exp)