# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017
# Implement Python Type Safety annotations
# Goldbach's Other Conjecture

# Every Odd Composite Number can be written as the sum of a prime and twice a square
# n = p + x^2 where p is prime

import math

# Upgraded faster prime test
def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w

    return True

def problem46():
    n = 1
    while True:
        n += 2
        if prime(n):
            continue
        b = False
        # So n is odd and not prime i.e. odd composite
        for p in range(2,n):
            if not prime(p):
                continue
            s = math.sqrt((n-p)//2)
            if 2 * int(s) * int(s) == n-p:
               b = True

        if not b:
            return n

print(problem46())
