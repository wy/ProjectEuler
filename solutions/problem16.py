# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Power Digit Sum

x = pow(2,1000)
y = str(x)
acc = 0
for i in y:
    y_int = int(i)
    acc = acc + y_int

print(acc)
