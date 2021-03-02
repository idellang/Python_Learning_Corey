def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result


my_nums = square_numbers([1, 2, 3, 4, 5])
# print(my_nums)


# generators
def square_numbers_generator(nums):
    for i in nums:
        yield (i * i)


my_nums = square_numbers_generator(my_nums)

# for num in my_nums:
#     print(num)

# using list comprehension
my_num2 = [4, 3, 2, 1]

my_num2 = [num ** 2 for num in my_num2]
print(my_num2)

# just change to parenthesis
my_num2_generator = (num ** 2 for num in my_num2)
print(my_num2_generator)

# print out all number in generator
print(list(my_num2_generator))

# generator is better with performance if you convert to list you lose that performance