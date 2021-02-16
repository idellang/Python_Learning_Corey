if False:
    print("Hello World")

language = "Python"
if language.startswith("P"):
    print("The language is python")

if language.startswith("P"):
    print("The language is python")
elif language.startswith("J"):
    print("The language is java")
else:
    print("No Match")

user = "Admin"
logged_in = False

if user == "Admin" and logged_in:
    print("Admin Page")
else:
    print("Bad Credentials")

print(not logged_in)

# is is True is two objects have the same memory
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
print(id(a))
print(id(b))


# False values in python
# False
# None
# zero for any numeric
# empty sequence '' () []
# empty mapping {}

condition = {"a"}

if condition:
    print("Evaluated to true")
else:
    print("Evaluated to false")

