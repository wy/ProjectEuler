# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

def problem1():
    # Check for divisors of 3 or 5, add to accumulator if so
    acc = 0
    for i in range(1,1000):
        if i % 3 == 0 or i % 5 == 0:
            acc = acc + i
    return acc

print(problem1())