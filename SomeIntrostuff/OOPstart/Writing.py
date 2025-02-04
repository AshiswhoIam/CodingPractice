import json
import csv
employees= ["Bib","Alex","Dong","Jemie"]
#txt_data="I like pizza"

file_path="SomeIntrostuff\\OOPstart\\output.txt"

#w write,x write if it odesnt exists, a append file, r to read
try:
    with open(file_path,"w") as file:
        for employee in employees:
            file.write("\n"+employee)
            
        #file.write("\n"+txt_data)
        print(f" txt file '{file_path}' was created ")
except FileExistsError:
    print("that file already exists")


#dictionary writing with json
capitals = {"USA": "Washington DC ",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

file_path2="SomeIntrostuff\\OOPstart\\caps.json"

try:
    with open(file_path2,"w") as file:
        json.dump(capitals,file,indent=4)

        print(f" json file '{file_path2}' was created ")
except FileExistsError:
    print("that file already exists")


#csv file

students=[['Name', 'Age', 'GPA'],
['Alice', 22, 3.75],
['Bob', 19, 2.91],
['Charlie', 24, 3.45],
['David', 20, 3.98],
['Emma', 21, 3.65],
['Fiona', 18, 3.12],
['George', 23, 3.80],
['Hannah', 25, 2.95],
['Isaac', 20, 3.50],
['Jack', 22, 3.67]]

file_path3="SomeIntrostuff\\OOPstart\\students.csv"

try:
    with open(file_path3,"w",newline="") as file:
        writer = csv.writer(file)
        for row in students:
            writer.writerow(row)
        print(f" csv file '{file_path3}' was created ")
except FileExistsError:
    print("that file already exists")
