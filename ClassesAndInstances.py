# blue print for creating instances


class Employee:
    pass


class Employee2:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def display_fullname(self):
        return f"{self.first} {self.last}"


emp_1 = Employee()
emp_2 = Employee()

emp_1.first = "Led"
emp_1.last = "Castaneda"
emp_1.email = "jfcastaneda@up.edu.ph"
emp_1.pay = 50000

emp_2.first = "Test"
emp_2.last = "User"
emp_2.email = "test_user@gmail.com"
emp_2.pay = 600000

# print(emp_1.email)
# print(emp_2.email)
# print(type(emp_1))

emp_3 = Employee2("Led", "Castaneda", 500)
emp_4 = Employee2("User", "Test", 10000)
print(emp_3.email)
# print(emp_3.display_fullname())
# print(emp_4.display_fullname())

# Can run methods using class name
# need to pass the instance
print(Employee2.display_fullname(emp_4))
# No need because it already passed self
print(emp_4.display_fullname())