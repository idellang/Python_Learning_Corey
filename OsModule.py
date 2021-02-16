# interact with the operating system
import os

print(os.getcwd())

# navigate to desktop
os.chdir(r"C:\Users\ROG\Desktop\LEARN\00PYTHON\Python_Corey")


print(os.listdir())

# create new folder
# os.makedirs("OS_demo_2/Sub_dir_1")

# os.removedirs("OS_demo_2/Sub_dir_1")
# print(os.listdir())

# rename
# os.rename("test.txt", "demo.txt")

# look at info about files
# print(os.stat("demo.txt"))

# entire directory tree
# for each directory, yields paths, directories within the path and files within that path
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("Current Path", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)


# access home directory by grabbing home environment variable
print(os.environ.get("HOME"))

# create file in the home directory
file_path = os.path.join(os.environ.get("HOME"), "test.txt")
print(file_path)

print(os.path.basename("/tmp/test.txt"))
print(os.path.dirname("/tmp/test.txt"))
print(os.path.split("/tmp/test.txt"))
print(os.path.exists("/tmp/test.txt"))
print(os.path.splitext("/tmp/test.txt"))