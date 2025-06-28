# lambda keyword is used to give a function to a kind of variable. It has no name on it owns
lambda a,s,d : a+s*d

cube = lambda a : a*a*a
square = lambda a: a*a
sum = lambda x,y,z : x+y+z
print(cube(4))
print(square(4))
print(sum(85686844,26853252,769623))

# Used when giving a function as an argument to another function
def func(fx ,c ):
    return 62 * fx(c)
print(func(lambda x : x*x*x*x,99))