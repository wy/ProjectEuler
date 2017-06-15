# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

import math
# Highly divisible triangular numbers

#Start with a simply triangular number generator

def triangular(n):
    acc = 0
    for i in range(1,n+1):
        acc = acc + i
    return acc

# then we need a function that calculates all the divisors
# crude method is just to iterate over all numbers less than n

def divisors(n):
    c = 1 # always divide by yourself
    for i in range(1,n):
        if n % i == 0:
            c = c + 1

    return c

# faster method for divisors
# note all divisors are paired apart from integer square roots

def divisors_2(n):
    c = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            c = c + 2

    if math.ceil(math.sqrt(n)) == math.floor(math.sqrt(n)):
        c = c + 1

    return c


def problem12():
    
    n = 0
    while True:
        n = n + 1
        s = triangular(n)
        if divisors_2(s) > 500:
            return s
