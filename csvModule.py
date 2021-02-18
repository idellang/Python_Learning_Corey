import csv

with open(
    "names.csv",
    "r",
) as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("new_names.csv", "w") as new_file:
        csv_writer = csv.writer(new_file, delimiter="\t")

        for line in csv_reader:
            csv_writer.writerow(line)


# with open("new_names.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter = '\t')

#     for line in csv_reader:
#         print(line)


# dict reader

# will convert to key values
with open("names.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line["email"])

with open("names.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open("new_names.csv", "w") as new_file:
        field_names = ["first_name", "last_name"]  # removed email
        csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter="\t")
        csv_writer.writeheader()  # write field names as first line

        for line in csv_reader:
            del line["email"]
            csv_writer.writerow(line)
