# Switch of cpp is replaced by Match in Python
x = int(input("Enter any integer below 10 : "))
match x:
    case 8:
        print("Fine !!!")
    case _:
        print("Default case running")
