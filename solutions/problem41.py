# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Pandigital Primes
# Find largest n-digit pandigital prime
# Obv it has to be 9 digits or less

# Use the isprime checker
# Easiest is to use permutations from #24

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

from itertools import permutations


def problem41():
    
    perms = [''.join(p) for p in permutations('1234567')]
    perms.sort()

    for p in perms[::-1]:
    
        if prime(int(p)):
            return p
    
    
