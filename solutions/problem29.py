# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Distinct Powers
# Find the size of the set S
# For all a^b fo 2<=a<=100 and 2<=b<=100
# S = {s = a^b | a,b in 2..100}

def problem29():
    
    powers = set()
    for a in range(2,101):
        for b in range(2,101):
            powers.add(pow(a,b))

    return len(powers)
