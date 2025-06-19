# Making change in tuple
tup = (1,2,3,4,5)
li = list(tup)
li.pop(3)
li.append(32)
li.append(88)
li[1] = 101
print (li)
tup2 = tuple(li)
print(tup2)

# Congatenate tuple
tup3 = tup + tup2
print(tup3)

# Operations on tuple
b = tup3.count(3)
print(b)

c = tup3.index(101)
print(c)