# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# a = (500000-1000b)/(1000-b)

def problem9():

    for b in range(1,999):
        a = (500000-1000*b)//(1000-b)
        a2 = (500000-1000*b)/(1000-b)
        if a == a2 and a < b:
            c = 1000 - b - a
            if b < c:
                return a * b *c
    
