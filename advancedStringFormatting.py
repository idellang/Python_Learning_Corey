person = {"name": "Jen", "age": 23}

# not readable
sentence = (
    "My name is " + person["name"] + " and I am " + str(person["age"]) + " yrs old."
)

print(sentence)

sentence = "My name is {} and I am {} yrs old".format(person["name"], person["age"])
print(sentence)

# can also explicitly number placeholders
# useful if theres a need to be repeated
sentence = "My name is {0} and I am {1} yrs old".format(person["name"], person["age"])
print(sentence)

# can also access values on the placeholders
# will pass dictionary to all placeholders
sentence = "My name is {0[name]} and I am {0[age]} yrs old".format(person)
print(sentence)

# also works for list
l = ["Jenn", 23]

sentence = "My name is {0[0]} and I am {0[1]} yrs old".format(l)
print(sentence)

# can access attributes in a similar way
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Jack", "33")

sentence = "My name is {0.name} and I am {0.age} years old".format(p1)
print(sentence)

# Pass keyword argument
sentence = "My name is {name} and I am {age} years old".format(name="Jenn", age="30")
print(sentence)

# unpack dictionary to format
sentence = "My name is {name} and I am {age} years old".format(**person)
print(sentence)

# format and printing numbers
# add padding to be 2 digits
for i in range(1, 11):
    sentence = "The value is {:02}".format(i)
    print(sentence)

# format for decimal places
pi = 3.14159265
sentence = "Pi is equal to {:.2f}".format(pi)
print(sentence)

# comma separators
sentence = "1 MB is equal to {:,.2f} bytes".format(1000 ** 2)
print(sentence)

# format and print out dates
import datetime

my_date = datetime.datetime(2016, 9, 24, 10, 30, 45)
print(my_date)

# March 01, 2016

sentence = "{:%B %d, %Y}".format(my_date)
print(sentence)

# March 01, 2016 fell on a tuesday and was the 061 of the yearr.

sentence = "{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} of the year".format(
    my_date
)
print(sentence)