# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

def prime(n, knownprimes):
    for i in knownprimes:
        if n % i == 0:
            return False
    else:
        return True

def problem7(n):
    i = 0
    knownprimes = []
    j = 2
    while i < n:
        if prime(j,knownprimes):
            knownprimes.append(j)
            i = i + 1
        j = j + 1
    return knownprimes[-1]
