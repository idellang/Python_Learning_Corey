student = {"name": "John", "age": 25, "courses": ["Math", "Comsci"]}

print(student)
# accessing element
print(student["name"])
print(student["courses"])

# accessing a key that doesnot exist
# print(student["number"])
print(student.get("number"))
print(student.get("name"))

# setting a defualt if none
print(student.get("number", "no number"))

# add entry to dictionary
student["phone"] = "555-5555"
print(student.get("phone"))

# update method
student.update({"name": "Jane", "age": 26, "phone": "555-555"})
print(student)

# delete a key
del student["age"]
print(student)

# student.pop("courses")
# print(student)

# looping through keys and values
print(len(student))  # prints number of keys
print(len(student.values()))  # check number of values
print(student.items())  # for key value pairs

for key, value in student.items():
    print(key)
    print(value)
