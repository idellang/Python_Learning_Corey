# inheritance - inherits attributes and methods from parent class
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


class Developer(Employee):
    # class variable
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    raise_amount = 1.15

    # dont pass mutable like list as default arguments
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_emp(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for emp in self.employees:
            print("-->", emp.display_fullname())

    def print_employee_pay(self):
        for emp in self.employees:
            print(f"{emp.display_fullname()} has a pay of  {emp.pay}")


dev_1 = Developer("Led", "Castaneda", 20000, "Python")
dev_2 = Developer("Test", "User", 20000, "R")

# Check the source of developer
# print(help(Developer))

# print(dev_1.pay)
# print(dev_1.raise_amount)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.prog_lang)
# print(dev_2.prog_lang)

emp_1 = Employee("Jane", "Dong", 200)

manager_1 = Manager("Sue", "Smith", 90000, [dev_1, dev_2])
manager_1.print_employees()

manager_1.add_emp(emp_1)
manager_1.print_employees()

# print(manager_1.pay)
# manager_1.apply_raise()
# print(manager_1.raise_amount)
# print(manager_1.pay)

# isinstance will tell you if an object is instance of class
print(isinstance(manager_1, Manager))
print(isinstance(manager_1, Employee))
print(isinstance(manager_1, Developer))

# is subclass, will tell if class is sublass
print(issubclass(Developer, Employee))

manager_1.print_employee_pay()