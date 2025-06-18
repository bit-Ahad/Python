# Required argument == that we give in simple function that are required
def func1 (a,b):
    return (a+b)/2

abc = 34
bcd = 53
print("Average through required arguments is ", func1(abc,bcd))

# Default parameter given in argument
def func2 (a=4,b=5):
    return (a*b)

print("Multiplcation through default parameter is ",func2())
c=3
d=3
print("Multiplication through required parameter is", func2(c,d))

# Keyword argument 
# Giving argument while calling function
print("Multiplication with keyword argument is ",func2(b=34,a=431))