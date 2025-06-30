# self tell abour current instance of class
class person:
    name = "Ahad"
    age = 19
    def get(self):
        print(f"{self.name} is name. And, Age is {self.age}")

a = person()
b = person()
print(a.name)
print(a.age)
b.name = "Ahaddddddd"
b.age = 4
b.get()
