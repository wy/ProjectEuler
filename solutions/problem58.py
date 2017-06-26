# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017
# Spiral Primes



import math

# Upgraded faster prime test
def prime(n : int) -> bool:
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

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

def problem58() -> int:

    primes = 0
    nonprimes = 1

    n = 1 # Size of current grid

    acc = 1

    while (n < 9 or primes/(primes+nonprimes) > 0.1):
        n += 2          # increase grid size by 2 each time
        acc += 1        # go right one
        acc += n-2      # go up to the top
        if prime(acc):
            primes += 1
        else:
            nonprimes += 1
        acc += n-1      # go to the far left
        if prime(acc):
            primes += 1
        else:
            nonprimes += 1
        acc += n-1      # go far bottom left
        if prime(acc):
            primes += 1
        else:
            nonprimes += 1
        acc += n - 1  # go far bottom left
        if prime(acc):
            primes += 1
        else:
            nonprimes += 1

    return n


print(problem58())