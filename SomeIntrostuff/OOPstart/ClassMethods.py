#takes op realted to class itself

#instance methods usually for operations on objs of class
#Static methods for general utility fncs that dont ened acces to data
#class methods for class elvel data or req access to class use cls as param

class Student:

    count =0
    total_gpa=0

    def __init__(self,name,gpa):
        self.name= name
        self.gpa=gpa
        Student.count+=1
        Student.total_gpa+=gpa

        #Instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"
    

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count==0:
            return 0
        
        else:
            return f"Avg gpa: {cls.total_gpa/cls.count:.2f}"
    

student1 = Student("Heather", 4.0)
student2 = Student("Alex", 2.34)
student3 = Student("Mia", 3.0)

print(Student.get_count())
print(Student.get_average_gpa())