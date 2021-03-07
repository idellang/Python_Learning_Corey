s1 = set([1, 2, 3, 4, 5])
s2 = {10, 11, 12}
empty_set = set()

# add value
s1.add(6)

# add multiple values
s1.update([7, 8, 9])
s1.update(s2)


# remove value
s1.remove(5)

# use discard to avoid keyerror
s1.discard(1000)
# print(s1)


s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

s4 = s1.intersection(s2, s3)
s5 = s1.difference(s2)
s6 = s1.symmetric_difference(s2)
# print(s4)
# print(s5)
# print(s6)

l1 = [1, 2, 3, 1, 2, 3]
l2 = list(set(l1))
# remove duplicates
# print(l2)

employees = ["Led", "Mark", "John", "April", "Jonathan", "Judy", "Jenn", "Jane"]
gym_members = ["April", "John", "Corey"]
developers = ["Judy", "Corey", "Led", "Jane", "April"]

gym_developers = set(gym_members).intersection(set(developers))
employees_only = set(employees).difference(gym_members, developers)
print(gym_developers)
print(employees_only)