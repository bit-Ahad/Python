#  Magic method : They let you define how objects of your class behave with built-in Python operations.

class employee:
    def __init__(self,c):
        self.name = c
    
    # For lenght
    def __len__(self):
        i = 0 
        for c in self.name:
            i+=1
        return i
    
    # It return object as a string
    def __str__(self):
        return f"Name is : {self.name}"
    
    # It make object callable
    def __call__(self, task=None):
        if task:
            return print(f"{self.name} is working on task {task}")
        else:
            return print(f"{self.name} is waiting for task")

a = employee("Ahad")
print(len(a))
print(a)
a("Code")
# a()