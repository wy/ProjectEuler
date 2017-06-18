# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017
# Implement Python Type Safety annotations
# Pentagonal Numbers difference

# After doing a bit of research, it turns out proof of optimality is not trivial
# So instead I settle for finding the first solution that mimises the sum Pj+Pk

import sys

def pentagonal(n : int) -> int:
    return (n * ((3*n) - 1)) // 2

def problem44():
    pentagonals = set()
    i = 1
    D = sys.maxsize
    while True:
        p = pentagonal(i)
        for Pj in pentagonals:
            if p - Pj in pentagonals and p - 2*Pj in pentagonals:
                if p-2*Pj < D:
                    D = p-2*Pj
        if D < sys.maxsize:
            return D
        pentagonals.add(p)
        i = i+1

    return D

print(problem44())



