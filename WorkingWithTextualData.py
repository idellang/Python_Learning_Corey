message = "Hello World"

message2 = "Bobby's World"

multiline_message = """
          This is a multiline message brought to you by Led's Burger.
          "This is the best", said one kid.
"""

# print(len(message))
# index 1
# print("Hello"[1])
# index 4
# print("Hello"[4])
print(message[0:5])
print("Hello World"[0:5])
# start with 0 if no value in the first
print(message[:5])

# string methods
print(message.lower())  # applies lower method on the string because string has methods.

# number of characters in string
print(message.count("o"))

# get the index
print(message.find("l"))  # will return -1 if it cant find it in the string

# replace character
new_message = message.replace("l", "1", len(message))
print(new_message)


# concatenating strings
greeting = "Hello"
name = "Led"
print(greeting + ", " + name + "." + "Welcome")

# string formatted
formatted_message = "{}, {}.Welcome!".format(greeting, name)
print(formatted_message)

# fstring
# advantage is that it can use functions inside f string
fstring_message = f"{greeting}, {name.upper()}. Welcome!"

print(fstring_message)

# check methods available to a variable
print(dir(fstring_message))

# getting help
print(help(str.count))