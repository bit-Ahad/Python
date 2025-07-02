# Instance variable is for objects
# Class Variable is for all objects of class
# Class variable is declared outside of constructor
# Changing class vaariable will generate a new instance for that specific instance

class employee:
    compname = "Hehe"
    numofemp = 0
    def __init__(self,nam):
        self.name = nam
        employee.numofemp+=1
    def get(self):
        print(f"Name is : {self.name} and he is working in Company : {self.compname}")
        print(f"Number of employee is : {self.numofemp}")

emp1 = employee("John")
emp1.get()
emp2= employee("Alex")
emp2.get()
emp3= employee("Matt")
emp3.get()