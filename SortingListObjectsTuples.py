li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_li = sorted(li)
print(s_li)

# will change variable
li.sort()
print(li)

# descending sorting
s_li = sorted(li, reverse=True)
print(s_li)

li.sort(reverse=True)
print(li)

# sorted function is more flexible because it works for not just on list
tup = (9, 1, 8, 2, 7, 3, 6, 3, 4, 5)
s_tup = sorted(tup)
print(s_tup)

di = {"name": "Led", "age": 25, "job": "analyst"}
s_di = sorted(di)
# sort keys
print(s_di)

# sort based on absolute value
li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li)
print(s_li)

# add key on sorting
s_li = sorted(li, key=abs)
print(s_li)

# for class objects you can use attrgetter to sort by attribute
