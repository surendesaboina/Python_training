num1 = 17
num2 = 0
try:
    num3 = num1 / num2
    print(num3)
except ZeroDivisionError:
    print('Cannot divide by Zero')
except:
    print('Some error occured')
finally:
    print('The object is deleted')
print('After the exception handling is done')