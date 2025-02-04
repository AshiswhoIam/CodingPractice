#reading txt json csv
import json
import csv

file_path="SomeIntrostuff\\OOPstart\\output.txt"

#open has file path and mode

try:
    with open(file_path,"r") as file:
        content= file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You dont have the perms to read that file")

file_path2="SomeIntrostuff\\OOPstart\\caps.json"

try:
    with open(file_path2,"r") as file:
        content2= json.load(file)
        print(content2)
        #print(content2["xxx"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You dont have the perms to read that file")

file_path3="SomeIntrostuff\\OOPstart\\students.csv"

try:
    with open(file_path3,"r") as file:
        content3= csv.reader(file)
        for line in content3:
            print(line[0])
        #can access index print(line[0])
     
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You dont have the perms to read that file")