import math as mt

def century(x):
    return mt.floor(x/100+1)

# Test
print(century(1350))