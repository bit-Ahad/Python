# It is first string written at first line inside a function , class etc

def fname (a,b):
    '''It is a docstring'''
    print (a*b**b*a+42)

print(fname.__doc__)
fname(9,4)
