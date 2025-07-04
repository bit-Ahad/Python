# These is used to check properties

# dir
x = [1,2,3]
print(dir(x))
print(x.__add__)


# __dic__   It return attributes as dictorany
class person:
    def __init__(self,a,b):
        self.name = a
        self.age = b

p = person("Ahad",19)
print(p.__dict__)

# Help gives a documentation of help
print(help(person))
