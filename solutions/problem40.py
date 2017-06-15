# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Champernowne's Constant


def genS():
    
    s = ""    
    L = 0
    i = 0
    while L < 10000001:
        s += str(i)
        L += len(str(i))
        i += 1

    return s

def problem40():

    s = genS()
    dprod = 1

    dprod *= int(s[1])
    dprod *= int(s[10])
    dprod *= int(s[100])
    dprod *= int(s[1000])
    dprod *= int(s[10000])
    dprod *= int(s[100000])
    dprod *= int(s[1000000])

    return dprod
