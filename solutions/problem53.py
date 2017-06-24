# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017
# Combinatoric Selections
import math

def nCr(n : int, r: int) -> int :
    nfact = math.factorial(n)
    rfact = math.factorial(r)
    nrfact = math.factorial(n-r)
    return nfact // (rfact * nrfact)

def problem53():
    cnt = 0
    for n in range(1,101):
        for r in range(1,n+1):
            if nCr(n,r) > 1000000:
                cnt += 1
    return cnt

print(problem53())