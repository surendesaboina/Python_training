class Employee:
    def __init__(self, name, designation, salary) -> None:
        self.name = name
        self.designation = designation
        self.salary = salary
    
    def __str__(self) -> str:
        return f'{self.name}, {self.designation}, {self.salary}'
    
emp = Employee('prakash','runner',1000)
print(emp)
print(emp.salary)