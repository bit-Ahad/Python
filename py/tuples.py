# Tuples is same as list just [] replaced by ()
tup = (1,2,3,4,5)
print(type(tup))


#  Tuple can't be changed like given below
#  tup[0] = 1  # It is only for list...
#  tup2[2] = "Ahad"

if 4 in tup:
    print("4 is here")

# One tuple can be given to another unlike tuple
tup2 = tup[1:3]
print(tup2)
