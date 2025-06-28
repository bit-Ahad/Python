di1 = {1:23,2:64,3:56,4:84,5:44}
di2 = {5:88,6:13,7:34,8:96}

# Just like unioun but it replace the duplicate one
di1.update(di2)
print(di1)

# di2.clear()
# print("Di2 is cleared : ",di2)

di2.pop(8)
print(di2)

# del di2 

di["wow"]="Added one more"
print(di)

# Use copy function to copy otherwise it just generate a refrence
di3 = di2.copy()
print(di3)
