# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017
# Permuted Multiples

from itertools  import permutations

# Should have guessed this would be about 1/7

def problem52():
    i = 1
    while True:
        perms = [''.join(p) for p in permutations(str(i))]
        if not str(2*i) in perms:
            i += 1
            continue
        if not str(3*i) in perms:
            i += 1
            continue
        if not str(4*i) in perms:
            i += 1
            continue
        if not str(5*i) in perms:
            i += 1
            continue
        if not str(6*i) in perms:
            i += 1
            continue
        return i

print(problem52())
