# normal use of functions
def square(x):
    return x * x


def cube(x):
    return x * x * x


f = square(5)
print(f)

# set f to the function
# f is equal to a function
f = square
print(square)
print(f)
print(f(5))

# passing a function as argument


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)


# return a function from another function
def logger(msg):
    def log_message():
        print("log :", msg)

    return log_message


log_hi = logger("hi")
log_hi()
