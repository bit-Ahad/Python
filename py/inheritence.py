# super() refers to parent class
class employee:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def get(self):
        print(f"Name is {self.name} and age is {self.age}")
    
class updated(employee):
    def __init__(self, n, a, c):
        super().__init__(n, a)
        self.pay = c
    def get2(self):
        print(f"Name is {self.name} and age is {self.age} and pay is {self.pay}")

a = updated("Ahad",19,85000)
a.get2()