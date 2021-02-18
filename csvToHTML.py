import csv

html_output = ""
names = []

with open("patrons.csv", "r") as datafile:
    csv_data = csv.reader(datafile)

    # skip 2 lines
    next(csv_data)
    next(csv_data)

    for line in csv_data:
        if line[0] == "No Reward":
            break
        names.append(f"{line[0]} {line[1]}")

for name in names:
    print(name)

html_output += f"<p>There are currently {len(names)} public contributors. Thank You!<p>"

html_output += r"\n<ul>"

for name in names:
    html_output += f"\n\t<li>{name}</li>"
html_output += r"\n<\ul>"

# print(html_output)

# using dictReader and dictwriter
with open("patrons.csv", "r") as datafile:
    csv_data = csv.DictReader(datafile)

    next(csv_data)

    for item in csv_data:
        if item["FirstName"] == "No Reward":
            break
        names.append(f"{item['FirstName']} {item['LastName']}")

print(names)