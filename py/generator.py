def mygen():
    for i in range(332242442444):
        # Complex Calculations
        yield i

gen = mygen()
print(next(gen))
print(next(gen))
print(next(gen))