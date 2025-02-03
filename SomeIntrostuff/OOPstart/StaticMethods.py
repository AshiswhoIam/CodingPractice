#Static method=> belongs to class rather than obj from that class
#instance methods are for op on instance ex obj
#static methods best util fnc no need acess to class data

class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position

    def get_info(self):
        return f"{self.name}={self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager","Casher","Cook","Janitor"]
        return position in valid_positions
    

# dont need to do employee= Employee()

employee1= Employee("Ash","Manager")
employee2= Employee("Garen","Cook")
employee3= Employee("Stuart","Janitor")

print(Employee.is_valid_position("Cook"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())