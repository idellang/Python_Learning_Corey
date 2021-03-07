# iterable - something that can be looped over
nums = [1, 2, 3]
i_nums = iter(nums)
# looping in a list
# for num in nums:
#     print(num ** num)

# has this method if iterable
# print(dir(nums))

# iterator - object with a state so that it remembers where it is during iteration
# iterators also know where to get next value
# list has no state and no method next there it isnt an iterator
# print(dir(i_nums))
# print(i_nums)
# print(next(i_nums))


class MyRange(object):
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


nums = MyRange(1, 10)

for num in nums:
    print(num)

# generators are iterators but dunder methods are created automatically


def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


my_range(1, 10)
print(my_range(1, 10))
nums_generator = my_range(1, 10)
print(next(nums_generator))
print(next(nums_generator))
print("\n")
for num in nums_generator:
    print(num)