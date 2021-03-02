class Employee:

    num_employee = 0

    # setting up class variable
    raise_amount = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def display_fullname(self):
        return f"{self.first} {self.last}"

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @display_fullname.setter
    def display_fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @display_fullname.deleter
    def display_fullname(self):
        print("Delete name!")
        self.first = None
        self.last = None


emp_1 = Employee("John", "Smith")

emp_1.first = "Jim"
print(emp_1.first)
print(emp_1.last)
print(emp_1.display_fullname)
# did not change the email
print(emp_1.email)

# set a full name that will change first and last
emp_1.display_fullname = "Idel Castaneda"
print(emp_1.first)
print(emp_1.last)
print(emp_1.display_fullname)
print(emp_1.email)

del emp_1.display_fullname
print(emp_1.first)
print(emp_1.last)
print(emp_1.display_fullname)
print(emp_1.email)