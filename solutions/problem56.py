# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017
# Powerful Digit Sum

# maximise the digits sum of a^b for a,b < 100

def digitsum(n:int) -> int:
    s = str(n)
    d = 0
    for c in s:
        d += int(c)
    return d

def problem56():
    max = 0
    for a in range(99,0,-1):
        for b in range(99,0,-1):
            n = a ** b
            d = digitsum(n)
            if d > max:
                max = d
            if 9 * len(str(n)) < max:
                break
    return max

print(problem56())