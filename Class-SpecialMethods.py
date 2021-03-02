# Special methods
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

    # repr(emp)
    # representation of object
    def __repr__(self):
        return 'Employee("{}", "{}", "{}")'.format(self.first, self.last, self.pay)

    # display to end user
    def __str__(self):
        return "{} - {}".format(self.display_fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.display_fullname())

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


emp_1 = Employee("Led", "Castaneda", 20000)
emp_2 = Employee("Test", "User", 20000)

# print(emp_1)
# print(repr(emp_1))

# this is the same
# print(1 + 2)
# print(int.__add__(1, 2))
# print(str.__add__("1", "2"))

print(emp_1 + emp_2)
print(len(emp_1))