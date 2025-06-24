# It will always executed even if function returned value
# It has to be executed no matter what happens
def fun():
    try:
        li = [9761,238,376,443]
        x = int(input("Enter any index : "))
        print(li[x])
        return 1
    except:
        print("Some Error Occured")
        return 0
    finally: # It will always executed even if function returned value
        print("Finally is always executed.")

x = fun()
print ("Function is returning : ",x)

# Finally Always comes with try and except never alone