def f(val):
    return [(i, val / i) for i in range(1, int(val**0.5)+1) if val % i == 0]

from itertools import combinations
from fractions import Fraction

n = 1

for i in range(10**(n+2)):


print(total)
