def f1():
    print("From the function 1")

def f2():
    print("From the function 2")
    return "cisco"

var = 500

dict1 = {
        0: f1,
        1: f2,
        2: "December",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        21: var,
        9: "September",
        10: "October",
        11: "November"      
}
print(dict1.get(0,"Invalid Month")())
print(dict1.get(1,"Invalid Month")())
print(dict1.get(11,"Invalid Month"))
print(dict1.get(21,"Invalid Month"))