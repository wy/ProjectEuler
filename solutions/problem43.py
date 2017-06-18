# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Sub-string Divisibility

# 1406357289 is pandigital and has this odd prime divisibility feature

from itertools import permutations

def problem43():
    # Just loop through all possible pandigital numbers
    # Which is just all permutations of the 9-digit string 0123456789

    perms = [''.join(p) for p in permutations('0123456789')]
    perms.sort()

    acc = 0
    for p in perms:
        d = int(p)

        if not int(p[7:10]) % 17 == 0:
            continue
        if not int(p[6:9]) % 13 == 0:
            continue
        if not int(p[5:8]) % 11 == 0:
            continue
        if not int(p[4:7]) % 7 == 0:
            continue
        if not int(p[3:6]) % 5 == 0:
            continue
        if not int(p[2:5]) % 3 == 0:
            continue
        if not int(p[1:4]) % 2 == 0:
            continue

        print(d)
        acc += d

    return acc

print(problem43())



