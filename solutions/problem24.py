# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Lexicographic Permutations

# For 0,1,2,3,4,5,6,7,8,9
# Generate all permutations
# Convert them to a list of numbers
# Sort them in a list
# Get the 1 millionth one (which is actually index 1M-1

from itertools  import permutations
perms = [''.join(p) for p in permutations('0123456789')]

perms.sort()

print(perms[999999])
