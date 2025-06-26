# It just count index or number of times loop have been repeated

fruit = ["apple","banana","pineapple","again apple","another apple"]
# Return in tuple form (index,value)
for v in enumerate(fruit):
    print(v)

# i for index and j for value in list
for i,j in enumerate(fruit):
    print(i,j)
    if(i==2): #If index is equal to 2 then do some task
        print("Index 2 reached")