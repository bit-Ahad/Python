# Syntax :
# def my_decorator(func):
#     def wrapper():
#         # Code to run before the original function
#         print("Before the function runs")
#         func()
#         # Code to run after the original function
#         print("After the function runs")
#     return wrapper

def decorator(func):
    def fff(a, b):
        print("Hello Function is running....... ")
        func(a, b)
        print("Thanks for using functions !!!")
    return fff

@decorator
def sum(a, b):
    print("Sum is : ", a + b)

sum(47, 423)

# Desiiii Syntax
# def dec(fx):
#     def abd(*argu,**kwargu):
#         print("Phele Krna")
#         fx(*argu,**kwargu) # type: ignore
#         print("Bad ma krna")
#     return abd

# Decorator take a function modify it and return it