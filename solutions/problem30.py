# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Digit Fifth Powers
# The only trick here is realising how to calculate the limit
# For an n-digit number, the maximum number would be n * 9^5
# Which is 59049
# so the range is n=1 to n=6 because you can't generate a n-digit number with more than 6 digits

def digitgen(N,P):
    x = str(N)
    acc = 0
    for i in x:
        j = int(i)
        acc += pow(j,P)
    return acc

def problem30():
    acc = 0
    for i in range(2,1000000):
        if i == digitgen(i,5):
            acc += i
    return acc


