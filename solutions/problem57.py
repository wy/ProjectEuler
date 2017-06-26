# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017
# Square Root Convergents

# Looking at root 2 approximations

from typing import Tuple
from fractions import Fraction

def approximation(n: int) -> Fraction:
    # n ranges from 1 to infinity
    if n == 1:
        return Fraction(3,2)
    else:
        f = Fraction(1,1)
        f2 = Fraction(1,2)
        for i in range(1,n):
            f2 = 1/(2 + f2)

        return f + f2

def extract(f : Fraction) -> Tuple[int,int]:
    return f.numerator,f.denominator

def problem57():
    cnt = 0
    for i in range(1,1001):
        (n,d) = extract(approximation(i))
        if len(str(n)) > len(str(d)):
            cnt += 1
    return cnt

print(problem57())


