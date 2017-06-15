# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Amicable Numbers
# d(a) = b & d(b) = a where d(n) = proper divisors of n & a != b

def d(n):
    if n <= 1:
        return 0

    acc = 0
    for i in range(1,n):
        if n % i == 0:
           acc = acc + i

    return acc

acc = 0
for i in range(1,10000):
    x = d(i)
    if x > i and x < 10000 and d(x) == i:
        acc = acc + x + i

print(acc)
