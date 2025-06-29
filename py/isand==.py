# is compare exact location of memory
# == compare the value
a = [1,2,3]
b = [1,2,3]
print(a is b) # location
print(a == b) # value

print("\n----------\n")

a = 3
b = 3
print(a is b) # location
print(a == b) # value
# It gave both equal because python make a single constant in memory and give it to both a and b