

class Student:

    #class variable
    cyear=2024
    numstd=0

    def __init__(self,name,age):
        self.name=name
        self.age=age

        Student.numstd+=1

student1= Student("Keanu","45")
student2= Student("Rdj",32)
student2= Student("Ash",252)

print(student1.name)
print(student2.age)

#best not to use from a instance
print(Student.cyear)
print(Student.numstd)

print(f"The students of class year {Student.cyear} has {Student.numstd} people")
print()