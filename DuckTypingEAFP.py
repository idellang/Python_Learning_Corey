class Duck:
    def quack(self):
        print("Quack quack")

    def fly(self):
        print("Flap Flap")


class Person:
    def quack(self):
        print("I am quacking like a duck")

    def fly(self):
        print("I am flapping my arms")


def quack_and_fly(thing):
    # Not duck-typed (Not pythonic)

    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print("This has to be a duck!")

    print()


# d = Duck()
# quack_and_fly(d)

# p = Person()
# quack_and_fly(p)

# p.fly()


def quack_and_fly2(thing):
    # LBYL (non pythonic)

    if hasattr(thing, "quack"):
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing, "fly"):
        if callable(thing.fly):
            thing.fly()

    print()


# d = Duck()
# quack_and_fly2(d)

# p = Person()
# quack_and_fly2(p)


def quack_and_fly3(thing):
    # EAFP (pythonic)
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

    print()


# d = Duck()
# quack_and_fly3(d)

# p = Person()
# quack_and_fly3(p)

person = {"name": "Jess", "age": 23, "job": "programmer"}
person = {"name": "Jess", "age": 23}

# LBYL not pythonic
if "name" in person and "age" in person and "job" in person:
    print("I am {name}. I am {age} years old and I am a {job}".format(**person))
else:
    print("Missing some keys")

# EAFP (Pythonic)

try:
    print("I am {name}. I am {age} years old and I am a {job}".format(**person))
except KeyError as e:
    print("Missing {} key".format(e))
