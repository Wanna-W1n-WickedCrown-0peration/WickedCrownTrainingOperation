from math import gcd 
def egcd(a,b,c):
    assert(gcd(a, b) == c)
    x0, y0 = 1, 0 
    x1, y1 = 0, 1
    r0 = a
    r1 = b 
    while r1 != 0:
        q = r0 // r1 
        nr = r0 % r1 
        nx = x0 - q * x1 
        ny = y0 - q * y1 
        x0, y0 = x1, y1 
        x1, y1 = nx, ny 
        r0, r1 = r1, nr 
    return (x0, y0)
from random import randint
for i in range(100):
    a = randint(0, 100000)
    b = randint(0, 100000)
    c = gcd(a,b)
    x,y = egcd(a,b,c)
    print(f"Testing on {a = }, {b = }, {c = }")
    print(f"Result : {x = }, {y = }")
    assert(a * x + b * y == c)

