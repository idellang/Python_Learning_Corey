try:
    f = open("corrupt_file.txt")
    # var = bad_var
    if f.name == "corrupt_file.txt":
        raise Exception
except FileNotFoundError:
    print("This file does not exist")
except Exception as e:
    print('Error')
else:  # runs code if try does not raise exception
    print(f.read())
    f.close
finally:  # runs no matter what happens
    print("Executing Finally")
