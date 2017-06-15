# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Digit Factorials
import math

def curious(n):
    s = str(n)
    acc = 0
    for i in s:
        acc += math.factorial(int(i))
    return acc == n

def problem34():

    acc = 0
    for i in range(3,1000000):
        if curious(i):
            acc += i
    return acc
