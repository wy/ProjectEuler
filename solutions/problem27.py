# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Quadratic Primes
# n^2 + an + b for |a| < 1000 and |b| <= 1000
# where |n| is abs(n)

# Find a,b such that for n in (1...N): quad(n,a,b) is prime for maximal N

def quad(n,a,b):
    return n*n + a*n + b

def prime(n):

    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False

    return True

def consecutive(a,b):
    i = 1
    while True:
        if prime(quad(i,a,b)):
             i = i + 1
        else:
            return i

def problem27():
    max = (0,None)
    for a in range(-999,1000):
        for b in range(-1000,1000):
            res = consecutive(a,b)
            if res > max[0]:
                max = (res,(a,b))
                print(max)

    return max
