a = {1,2,3,4}
b = {4,5,6}

# Union
print(a.union(b))

# Intersection
print(b.intersection(b))

# Difference
print(a.difference(b)) 

# Disjoint Nothing in common
print(a.isdisjoint(b))

# Superset ... A is superset if all elements of B is in A
print(a.issuperset(b))

# Subset .. B is subset of A. If all elemnt of B is in A
print(a.issubset(b))

# to add a single item to set
a.add("Added")
print(a)

# To remove a item
a.remove("Added") #It generate error if not present
a.discard(4) #It don't generate error if not present
print(a)

# Remove a last item from set
a.pop()
print(a)

# a.clear() Clear all items 

# Given below updates original set
a.update(b)   
print(a)
a.intersection_update(b)
print(a)
a.difference_update(b)
print(a)
