class person:

    def __init__(self,a,b):
        self.name = a
        self.age = b
    
    def get(self):
        print(f"{self.name} is name. And, age is {self.age}")

a = person("Ahad",4)
a.get()
b = person("Ahad",34)
b.get()