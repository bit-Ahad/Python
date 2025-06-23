# We dont want the program to terminate if there is a error so we do error handling
num = input("Enter the number : ")
print(f"Table of {num} is ")

try:
    for i in range(1,11):
        print(f"{num} *",i," = ",int(num)*i)

except ValueError:  #occur due to wrong data type
    print("Enter a Integer")

except Exception as a:  #Give error back
    print(a)

except IndexError:  #Used for list
    print("Wrong Index")