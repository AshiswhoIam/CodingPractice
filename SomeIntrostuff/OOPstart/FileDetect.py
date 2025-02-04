import os

file_path="SomeIntrostuff\\OOPstart\\test.txt"

if os.path.exists(file_path):
    print(f"the location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesnt exists")