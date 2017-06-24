# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017
# Consecutive Prime Sum

# We need to iterate through the list of primes below 1 million / 21.

# Upgraded faster prime test
def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w

    return True

def primegenerator():
    primearr = [2]
    max = 1000000//21
    for i in range(3,max,2):
        if prime(i):
            primearr.append(i)

    return primearr

def problem50():
    maxlen = 0
    maxacc = 0
    primearr = primegenerator()
    length = len(primearr)
    for i in range(0,length):
        j = i
        acc = primearr[j]
        while (acc < 1000000 and j+1 < length):
            j += 1
            run = j - i
            if prime(acc) and run > maxlen:
                maxlen = run
                maxacc = acc
            acc += primearr[j]

    return maxacc



print(problem50())
