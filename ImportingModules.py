import my_module as mm
import sys
import random
import math
import datetime
import calendar
import os

# import function only
from my_module import find_index

# import everything

from my_module import *

courses = ["History", "Math", "Physics", "Compsci", "Bob's"]

# print(find_index(courses, "History"))

random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(rads)
print(math.sin(rads))


today = datetime.date.today()
print(today)

print(calendar.isleap(2017))

print(os.getcwd())

# get the location of the module
print(os.__file__)