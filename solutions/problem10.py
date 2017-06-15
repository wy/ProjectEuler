# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

def prime(n, knownprimes):
    for i in knownprimes:
        if n % i == 0:
            return False
    else:
        return True

def problem10(n):
    i = 0
    knownprimes = []
    j = 2
    acc = 0
    while j < n:
        if prime(j,knownprimes):
            knownprimes.append(j)
            acc = acc + j
            
        j = j + 1

    return acc
