import random

# 0 to 1
value = random.random()
print(value)

# floating value between 1 to 10
value = random.uniform(1, 10)
print(value)

# random integer
value = random.randint(1, 6)
print(value)

# choice picks from a list
greetings = ["hello", "hi", "hey", "howdy", "hola"]
rand_greetings = random.choice(greetings)
print(rand_greetings + " Led")

# multiple random values from list, can add weights

colors = ["red", "black", "green"]
rand_colors = random.choices(colors, weights=[18, 18, 2], k=10)
print(rand_colors)

# shuffle list values
deck = list(range(1, 53))
random.shuffle(deck)

hand = random.sample(deck, k=5)
print(hand)