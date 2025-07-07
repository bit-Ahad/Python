class io:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return f"After Addition : \nx is : {self.x+other.x}    y is : {self.y+other.y}"
    
a = io(529,643)
b = io(324,798)
print(a+b)

# Operator	Method	Example
# +	__add__(self, other)	a + b
# -	__sub__(self, other)	a - b
# *	__mul__(self, other)	a * b
# /	__truediv__(self, other)	a / b
# ==	__eq__(self, other)	a == b
# <	__lt__(self, other)	a < b
# >	__gt__(self, other)	a > b