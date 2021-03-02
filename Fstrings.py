first_name = "idel"
last_name = "castaneda"

sentence = "My name is {} {}".format(first_name, last_name)
# print(sentence)

f_sentence = f"My name is {first_name.upper()} {last_name.upper()}"
# print(f_sentence)

person = {"name": "Jenn", "age": 23}
sentence = "My name is {} and I am {} years old".format(person["name"], person["age"])
# print(sentence)

f_sentence = f"My name is {person['name']} and I am {person['age']} years old"

calculation = f"4 times eleven is equal to {4 * 11}"
print(calculation)

for n in range(1, 11):
    sentence = f"the value is {n:02}"
    print(sentence)

pi = 3.14159265
sentence = f"Pi is equal to {pi:.4f}"
print(sentence)

from datetime import datetime

birthday = datetime(1995, 12, 5)

sentence = f"My birthday is on {birthday:%B %d, %Y}"
print(sentence)