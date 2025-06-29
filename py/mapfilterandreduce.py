li = [1,2,3,4,5,6,7]

# All three of them take a function and a iterable(list) as argument 

# Map : It perform the function on each value of list
mli = map(lambda x: x*x,li)
print(list(mli))

# Filter : It Filter the items that not fullfil requirement 
fli = filter(lambda x: x%2 == 0,li)
print(list(fli))

# Reduce : Reduce it to one item
from functools import reduce
reduced = reduce(lambda x,y: x*y,li)
print(reduced)