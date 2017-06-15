# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

import math

x = math.factorial(100)
s = str(x)
acc = 0
for i in s:
    a = int(i)
    acc = acc + a

print(acc)
    
