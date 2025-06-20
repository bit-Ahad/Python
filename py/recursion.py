# Recursion == Calling same function in function body

# Factorial 5! = 5*4*3*2*1
# factorial(n)= n * factorial(n-1)

def fact(n):
    if (n==0 or n ==1):
        return 1
    else:
        a = n * fact(n-1)
        return a

a = int(input("Enter any number : "))
f = fact(a)
print("Factorial of is : ",f)

# Fibonaci   ====    0 1 1 2 3 5 8 13 ....

def fibonacci(n):
    if n == 0:
        return 0      # base case
    elif n == 1:
        return 1      # base case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # recursive call

# Ask user to enter how many numbers they want
num = int(input("Enter how many Fibonacci numbers you want: "))

# Print that many Fibonacci numbers
for i in range(num):
    print(fibonacci(i), end=" ")
