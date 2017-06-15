# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

def isPrime(n):
    #Prime if 2..n-1 does not divide n
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def primes(n):
    #returns primes from 2..n
    arr = []
    for i in range(2,n+1):
        if isPrime(i):
            arr.append(i)
    return arr

def primeFactors(n, primes):
    #returns number of times each of the primes in primes divides n
    arr = []
    
    for i in primes:
        j = n
        acc = 0
        while j % i == 0:
            acc = acc + 1
            j = j // i
        arr.append(acc)
    return arr

def multiplyOut(currentMax, primes):
    acc = 1
    for i in range(0, len(currentMax)):
        acc = acc * primes[i]**currentMax[i]
    return acc

def merge(currentMax, primeFactors):

    c = []
    for i in range(0, len(currentMax)):
        if currentMax[i] > primeFactors[i]:
            c.append(currentMax[i])
        else:
            c.append(primeFactors[i])
    return c

def problem5(n):
    #Populate the list of primes
    p = primes(n) # array of primes
    currentMax = primeFactors(n, p)

    for i in range(1,n):
        pf = primeFactors(i, p)
        currentMax = merge(currentMax, pf)

    return multiplyOut(currentMax, p)
    


#Brute force - too slow
def problem5brute(n):
    i = n
    while True:
        b = True
        for j in range(1,n+1):
            if i % j != 0:
                b = False
        if b:
            return i
        i = i + 1
