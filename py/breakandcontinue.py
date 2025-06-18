# Continue statment        # It skip a single iteration
for i in range(5):
    if(i==2 or i==3):
        continue
    print(i,"is value of i")
# Break statment           # It break the loop
for i in range(1,10):
    if(i==6):
        break
    print("5 x ",i," = ",5*(i))