def hello_func():
    print("Hello Function!")


# hello_func()

# for i in range(5):
#      hello_func()


def hello_func(greeting, name="You"):
    return f"{greeting}!, {name}"


print(hello_func("Hello", "Led"))

# args are positional arguments
# kwargs keyword values.
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info("Math", "Art", name="John", age=22)

courses = ["Math", "Art"]
info = {"name": "John", "age": 22}

# unpack list and dictionary
student_info(*courses, **info)


# Function that determines the day of month given a month and a year
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):

    if not 1 <= month <= 12:
        return "invalid year"

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(days_in_month(2018, 2))
