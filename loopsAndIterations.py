nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

# break : break out of the loop
for num in nums:
    print(num)
    if num == 3:
        print("We found the number three")
        break

# continue: move onto the next iteration
for num in nums:
    print(num)
    if num == 3:
        print("Found the number three")
        continue

# loop within a loop
for num in nums:
    for letter in "abc":
        print(num, letter)

# loop within a certain number of time
for i in range(1, 11):
    print(i)

# while loops : will keep going until certain condition is met
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
