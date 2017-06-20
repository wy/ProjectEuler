# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017
# Big Numbers

def problem48():
    acc = 0
    for i in range(1,1001):
        acc += i ** i
        acc = acc % 10 ** 10

    return acc

print(problem48())