# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

def problem6(n):
    #difference between sum of squares and squre of sum
    #this is just 2x sum of all product of non-identical pairs from 1 to n
    acc = 0
    for i in range(1,n+1):
        for j in range(i+1, n+1):
            acc = acc + i * j
    return 2 * acc
