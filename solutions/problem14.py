# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Collatz Sequence
# Numbers under 1 million

def collatz(n):
    """returns length of sequence"""

    acc = 0
    m = n
    while True:
        acc = acc + 1
        if m == 1:
            return acc
        else:
            if m % 2 == 0:
                m = m // 2
            else:
                m = 3*m + 1
                
def problem14():
    max = 0
    max_i = 0
    for i in range(1,1000000):
        m = collatz(i)
        if m > max :
            max = m
            max_i = i

    return max_i
    
