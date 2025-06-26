# GLobal Variable 
x = int(input("Enter any number for Global x : "))
print("value of Global x is : ",x)

def fun():
    # Local Variable
    local_x = int(input("Enter any number for Local x : "))
    print("Value of Local x is : ",local_x)
    # Accesing and Changing Global x
    global x
    print("Global X value again is : ",x)
    print("Now changing Global X  ")
    x=999999
    print("After Changing Global X is : ",x)

fun()
print("GLobal x outside function is : ",x)