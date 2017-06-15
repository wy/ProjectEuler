# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# 1000-digit Fibonacci Number
# Find N where len(Fib(N)) = 1000 and N smallest such solution

# Given monotonically non-decreasing, just iterate from Fib(1) upwards.

def problem25():
    Fprev = 1
    Fcurr = 1

    index = 2

    while True:
        index = index + 1
        Fnew = Fcurr+Fprev
        Fprev = Fcurr
        Fcurr = Fnew
        if len(str(Fnew)) == 1000:
            return index
    
