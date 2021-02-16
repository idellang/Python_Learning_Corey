import os

os.chdir(r"Files")
print(os.getcwd())

for file in os.listdir():
    f_name, f_ext = os.path.splitext(file)

    f_title, f_num = f_name.split(" ")

    # remove whitespace
    f_title = f_title.strip()
    f_num = f_num.strip()[1:].zfill(2)

    new_name = "{}-{}{}".format(f_num, f_title, f_ext)
    os.rename(file, new_name)
