# easier and readable way to create a list

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# list comprehension
my_list = [n for n in nums]
print(my_list)

# n^2 for each n
print([n ** 2 for n in nums])

# map + lambda
# map runs everything in a list using function and lambda is an anonymous function
my_list = map(lambda n: n * n, nums)
print(list(my_list))

# n for each n is nums is even
my_list = [n for n in nums if n % 2 == 0]
print(my_list)

# filter + lambda
my_list = map(lambda n: n % 2 == 0, nums)
print(list(my_list))
my_list = filter(lambda n: n % 2 == 0, nums)
print(list(my_list))

# (letter, num) pair for each letter in abcd and 0123
my_list = [[letter, num] for letter in "abcd" for num in range(4)]
print(my_list)


# Dictionary comprehension
names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]

print(list(zip(names, heros)))

# dictionary comprenhension using zip
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
# print(my_dict)

my_dict = {name: hero for name, hero in zip(names, heros)}
print(my_dict)

# dont add peter to the list
my_dict = {name: hero for name, hero in zip(names, heros) if name != "Peter"}
print(my_dict)

# set comprehension
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
my_set = set()

for n in nums:
    my_set.add(n)
# print(my_set)

my_set = {n for n in nums}
print(my_set)

# generator expression
# yield n*n for each n in nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def gen_func(nums):
    for n in nums:
        yield n * n


my_gen = gen_func(nums)
print(my_gen)
print(list(my_gen))

my_gen = (n * n for n in nums)
print(my_gen)
print(list(my_gen))