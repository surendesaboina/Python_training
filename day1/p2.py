# Check avg_score of Student marks and decide score

input_num1 = int(input('Enter 1st number:'))
input_num2 = int(input('Enter 2nd number:'))
input_num3 = int(input('Enter 3rd number:'))

avg_score = (input_num1 + input_num2 + input_num3)/3

if avg_score >= 0 and avg_score <= 100:
    if avg_score <= 49:
        print("Fail")
    elif avg_score <= 74:
        print("SC")
    elif avg_score <= 90:
        print("FC")
    else:
        print("Distiction")
else:
    print("Invalid")