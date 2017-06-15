# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

def prime(n):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    else:
        return False

def smallestprimedivisor(p):
    for i in range(2,p):
        if p % i == 0 and prime(i):
            return i
    return p

def problem3(p):
    largestprime = 0
    curr = p
    while curr > 1:
        print(curr)
        # find the first prime divisor of p
        largestprime = smallestprimedivisor(curr)
        while curr % largestprime == 0:
            curr = curr // largestprime
    return largestprime
        
    
