courses = ["Math", "History", "Physics", "Compsci"]
# print(courses)
# getting length
# print(len(courses))
# indexing
# print(courses[0])
# print(courses[len(courses) - 1])
# print(courses[-1])

# first index is inclusive but the second index is not
# print(courses[:2])
# if you leave one end point as blank, it will assume start or end
# print(courses[2:])

# add item to list
# courses.append("Art")  # will add at last
# print(courses)

# add onto an index
# courses.insert(0, "Art")
# print(courses)

# extend when u want to add multiple values.
# courses_2 = ["Art", "Education", "Music"]

# courses.insert(0, courses_2)
# print(courses)
# print(courses[0]) #will return list instead

# courses.extend(courses_2)
# print(courses)

# remove some list elements
# courses.remove("Math")
# print(courses)

# will remove last value
# popped = courses.pop()
# print(popped)
# print(courses)

# sort list
print(courses)
courses.sort()  # will not return an object
print(courses)
courses.reverse()
print(courses)

nums = [1, 5, 4, 3]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

# use sorted function if you want to return list
nums_2 = [1, 5, 7, 2, 3]
nums_2_sorted = sorted(nums_2)
print(nums_2)
print(nums_2_sorted)

print(min(nums_2))
print(sum(nums))
print(min(courses))  # works also

# find index of a certain value
print(courses.index("Compsci"))

# if in the list
print("Art" in courses)

# Looping through each value on list
for item in courses:
    print(item)

for num in nums:
    print(num)
    num += 1
    print(num)

# also good to know the index that you are on
# will return index and the value in a tuple
for course in enumerate(courses):
    print(course)

# can specify which value to start on
for course in enumerate(courses, start=1):
    print(course)

# string to list
# must use separator first then use the string function join
course_str = ",".join(courses)
print(course_str)

# string to list
new_list = course_str.split(",")
print(new_list)

# tuples are immutable
list1 = ["history", "math", "physics", "compsci"]
list2 = list1


print(list1)
print(list2)

list1[0] = "art"
print(list1)
print(list2)

# use tuple for objects you dont want to change
tuple1 = ("history", "math", "physics", "compsci")
tuple2 = tuple1
# tuple1[0] = "art" will result to error
print(tuple1)
print(tuple2)

for item in tuple1:
    print(item)

# sets are unordered and no duplicates
# uses curly braces
cs_courses = {"History", "Math", "Physics", "Compsci", "Math"}
art_courses = {"History", "Math", "Art", "Design"}
print(len(course))
print(cs_courses)

# sets do membership test faster
print("Math" in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.union(art_courses))

# create empty list tuples or list
empty_list = []
empty_list = list()
empty_list.append("appended")
print(empty_list)

# for empty sets
empty_set = set()