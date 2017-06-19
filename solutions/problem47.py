# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017
# Implement Python Type Safety annotations
# Distinct Prime Factors

# We need a way of doing prime factor decomposition
from typing import List
import math

# Upgraded faster prime test
def isPrime(n):
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

def distinctFactorsFast(p : int, knownprimes : List[int]) -> int:
    factors = set()
    i = 2
    n = p
    j = 0
    if len(knownprimes) == 0:
        knownprimes.append(3)
    while n > 1:
        if n % i == 0:
            n //= i
            factors.add(i)
            if len(factors) > 4:
                return 5 # This will fail the test so faster exit than generating all answers
        else:
            if i < knownprimes[-1]:
                i = knownprimes[j]
                j += 1
            else:
                i += 1
                nsqrt = math.sqrt(n)
                while (i < nsqrt and not isPrime(i)):
                    i += 1
                knownprimes.append(i)
    return len(factors)

def problem47():
    i = 1
    knownprimes = []
    while True:
        if distinctFactorsFast(i+3,knownprimes) == 4:
            if distinctFactorsFast(i+2,knownprimes) == 4:
                if distinctFactorsFast(i+1,knownprimes) == 4:
                    if distinctFactorsFast(i,knownprimes) == 4:
                        return i
                    else:
                        i += 1
                else:
                    i += 2
            else:
                i += 3
        else:
            i += 4

print(problem47())