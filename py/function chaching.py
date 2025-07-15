# Function chaching for memoziation to store the reslut of a function with a specific input and then re-use it
from functools import lru_cache
import time 
@lru_cache(maxsize=None)
def fib(n):
    time.sleep(1)
    if n<2:
        return n 
    return fib(n-1) + fib(n-2)

# print(fib(20))
# print(fib(34))
print(fib(14))
# again calling same
# print(fib(20))
# print(fib(34))
print(fib(14))