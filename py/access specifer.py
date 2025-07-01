#  Public Private Protected
#  Access Modifiers can be used with both functions and variables
class employee:
    def __init__(self,n,a,f):
        self.age = a    # Public
        self.__name = n   # Private
        self._pay = f
    def _get(self):
        print(f"Age is : {self.age} Name is {self.__name} Pay is {self._pay}")

a = employee("Ahad", 23 , 383930)
# Public : 
print(a.age)  # Can be accessed because it is public

# Private : 
# print(a.__name)  Can't be accessed like this
print(a._employee__name)
# It is called name mangling

# Protected
# protected can be used outside class but it is not recmonded
a._get()
