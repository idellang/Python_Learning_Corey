import datetime


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

    # receive class as first argument instead of instance
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        # create new employee
        return cls(first, last, pay)

    # static methods are regular functions within a class
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


emp_1 = Employee("Led", "Castaneda", 5000)
emp_2 = Employee("Test", "User", 5000)


Employee.set_raise_amt(1.05)
# is equal to
# Employee.set_raise_amt = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


emp_str_1 = "John-Doe-7000"
emp_str_2 = "Steve-Smith-2000"
emp_str_3 = "Jane-Doe-9000"

# works but corny
# first, last, pay = emp_str_1.split("-")
# new_emp_1 = Employee(first, last, pay)
# print(new_emp_1.display_fullname())

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.display_fullname())

my_date = datetime.date(2021, 2, 19)
print(Employee.is_workday(my_date))