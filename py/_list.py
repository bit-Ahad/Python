# list
mak = [14, 2, 3, "Ahad", 232, "das"]
print(mak)

# Indexs can be used with list just like string
print(mak[1:4])
print(mak[1:5:2]) #start stop step
print(mak[:])  #Complete list printed

# Checking in list
if "Ahad" in mak:
    print("Yes")
else:
    print("No")

# List compresion
list1 = [i*i for i in range(5)]
print(list1)
list2 = [i*i for i in range(5) if i%2 == 0]
print(list2)