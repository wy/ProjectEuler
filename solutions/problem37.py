# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Truncatable Primes

# Truncatable in both directions
# The maths part is interesting... how high do you go?

# We can just generate them
# e.g. the first digit must be 3 or a 7.
# because if it was 5, then any multi digit would divide 5.

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

def truncatable_left(n):
    if not prime(n):
        return False

    if n < 10:
        return True

    return truncatable_left(int(str(n)[1:]))
    

    
def truncatable_right(n):
    if not prime(n):
        return False

    if n < 10:
        return True

    return truncatable_right(n//10)    


def truncatable(n):
    s = str(n)
    if "0" in s:
        return False
    if "4" in s:
        return False
    if "6" in s:
        return False
    if "8" in s:
        return False
    if not prime(n):
        return False

    return truncatable_left(n) and truncatable_right(n)

        

def problem37():

    # We know there are only 11 of these

    i = 11
    count = 0
    acc = 0
    while count < 11:
        if truncatable(i):
            count += 1
            acc += i
            print(i)
        i += 2
    return acc


