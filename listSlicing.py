mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(mylist)

print(mylist[-1])

# list[start:end:step]
print(mylist[0:6])
print(mylist[3:8])

# can mix and match positive and negative index
print(mylist[3:-2])

# if left blank, it will assume to end
print(mylist[1:])
print(mylist[:8])

# step will skip some values
print(mylist[2:-1:2])

# -step will run in reverse
print(mylist[-1:2:-1])

# entire list reverse
# same as end to end reverse
print(mylist[::-1])

my_string = "I am Led Castaneda"
print(my_string[::-1])

print(my_string[9:])