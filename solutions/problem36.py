# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Double-base Palindromes

# 585 = 1001001001_2
# Look for numbers < 1M which are palindromes in base 10 and base 2
# Ignore leading 0's so any number ending in a 0 is auto-excluded
# Find the sum

def ispalindrome(n):
    if n % 10 == 0 :
        return False
    if n % 2 == 0:
        return False
    s = str(n)
    b = bin(n)[2:]
    if str(n) == str(n)[::-1] and b == b[::-1]:
        return True
    return False

def problem36():
    acc = 0

    for i in range(1,1000000):
        if ispalindrome(i):
            acc += i
    return acc


    
