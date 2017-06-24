# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017
# Prime Permutations

from itertools  import permutations


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

def problem49():

    for i in range(1000,9999):
        if not prime(i):
            continue
        if not prime(i+3330):
            continue
        if not prime(i+6660):
            continue
        #Possible solution
        if i == 1487:
            continue # known solution

        perms = [''.join(p) for p in permutations(str(i))]
        if str(i+3330) not in perms:
            continue
        if str(i+6660) not in perms:
            continue
        return str(i)+str(i+3330)+str(i+6660)

print(problem49())

