f = open("test.txt", mode="r")

print(f.name)
print(f.mode)

f.close()

# open the file using context manager
with open("test.txt", "r") as f:
    f_contents = f.read()
    print(f_contents)

# readlines will return list
with open("test.txt", "r") as f:
    f_contents = f.readlines()
    print(f_contents)

# readline will grab the first line
with open("test.txt", "r") as f:
    f_contents = f.readline()
    print(f_contents, end="")

    f_contents = f.readline()
    print(f_contents, end="")

# will not all at once
with open("test.txt", "r") as f:
    for line in f:
        print(line, end="")

# can specify in f.read the amount of data to read at a time
# with open("test.txt", "r") as f:
#     f_contents = f.read(100)
#     print(f_contents)

# will start at zero
with open("test.txt", "r") as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end="")
    f.seek(0)
    print(f_contents)

    # while len(f_contents) > 0:
    #     print(f_contents, end="*")
    #     f_contents = f.read(size_to_read)

# with open("test2.txt", "w") as f:
#     f.write("Test")
#     f.seek(0)
#     f.write("Test2")

with open("test.txt", "r") as rf:  # read file
    with open("testcopy.txt", "w") as wf:  # writing copy
        for line in rf:
            wf.write(line)

# for images, open file in binary mode
with open("image.png", "rb") as rf:  # read file
    with open("imagecopy.png", "wb") as wf:  # writing copy
        for line in rf:
            wf.write(line)

# per chunk
# for images, open file in binary mode
with open("image.png", "rb") as rf:  # read file
    with open("imagecopy.png", "wb") as wf:  # writing copy
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)