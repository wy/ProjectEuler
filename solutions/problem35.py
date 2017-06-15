# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Circular Primes
# Need to use a rotation method, let's write one

def rotations(n):
    rot = []
    s = str(n)
    length = len(s)

    if "0" in s or "2" in s or "4" in s or "6" in s or "8" in s:
        return []
    

    for i in range(0,length):
        rot.append(n)
        n2 = n % 10
        n = n // 10
        n = n + (n2 * 10**(length-1))

    return rot

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

def primeArr(arr):
    for i in arr:
        if not prime(i):
            return False

    return True

def problem35():
    cnt = 0 

    for i in range(2,1000000):
        if not prime(i):
            continue
        if i < 10:
            cnt += 1
            print(i)
            continue
        rot = rotations(i)
        if len(rot) == 0:
            continue
        if primeArr(rot):
            cnt += 1
            print(i)

    return cnt
        
