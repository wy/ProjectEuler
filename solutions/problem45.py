# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017
# Implement Python Type Safety annotations
# Triangle, Pentagonal and Hexagonal



def triangle(n : int) -> int:
    return (n * (n+1)) // 2

def pentagonal(n : int) -> int:
    return (n * ((3*n) - 1)) // 2

def hexagonal(n : int) -> int:
    return n * ((2*n)-1)

def problem45():
    t = 286
    p = 1
    h = 1
    P = pentagonal(p)
    H = hexagonal(h)
    while True:

        T = triangle(t)
        while(P < T):
            p += 1
            P = pentagonal(p)

        while(H < T):
            h += 1
            H = hexagonal(h)

        if P == T and H == T:
            return T

        t += 1

print(problem45())