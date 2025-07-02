# When using a simple function inside class. A function that have no use of self.
# can use it by using class name or instance name 
class hi:
    def __init__(self,name):
        self.name = name
    

    @staticmethod
    def sum(a,b):
        return a+b
    
obj = hi("Ahad")
print(obj.sum(232,796))     # Using instance name with function
print(hi.sum(28,69))        # Using class name with function


# We use static method because if we are gonna share a class with someone this function will also be share