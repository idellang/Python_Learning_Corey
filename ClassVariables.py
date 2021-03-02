# class variable : data shared by all classes
class Employee:

    num_employee = 0

    # setting up class variable
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_employee += 1

    def display_fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("Led", "Castaneda", 5000)
emp_2 = Employee("Test", "User", 5000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

print(Employee.raise_amount)
# accesses Employee raise amount because the instance dont have
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# no raise amount
print(emp_1.__dict__)
# there's raise amount
print(Employee.__dict__)

# Raise employee raise
emp_1.raise_amount = 1.05
print(emp_1.__dict__)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)

print(Employee.num_employee)