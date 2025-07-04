# It is used to call a parent class method in cho;d class
# super().get()

class person:
    def __init__(self,a):
        self.name = a
    def print(self):
        print("Name is : ",self.name)

class person2(person):
    def __init__(self , a, b):
        super().__init__(a)
        self.age = b
    def print(self):
        super().print()
        print("Age is : ",self.age)
     
a = person2("Ahad",39)
a.print()