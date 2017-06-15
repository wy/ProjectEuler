# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

#26 - Reciprocal Cycles
#Learnt some new maths here

import itertools
#finds the first number in the sequence (9,99,...) that is divisible by x
def find_divisible_repunit(x):
    assert x%2!=0 and x%5 != 0
    for i in itertools.count(1):
        repunit = int("9"*i)
        if repunit % x == 0:
            return repunit

def form(denominator):
    numerator = 1
    shift = 0
    for x in (2,5):
        while denominator % x == 0:
            denominator //= x
            numerator *= (10/x)
            shift += 1 # this is a factor of 10 power shift
    repunit = find_divisible_repunit(denominator)
    return len(str(repunit))

def problem26():
    max = (1,1)
    for i in range(1,1001):
        x = form(i)
        if x > max[0]:
            max = (x,i)

    return max
    
