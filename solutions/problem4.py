# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

def palindrome(n):
    j = str(n)
    for i in range(len(j)//2):
        if j[i] != j[len(j)-1-i]:
            return False
    return True
    
def problem4():
    # Try all 3 digit pairs
    # Got to be careful with how you iterate
    # Need to create a Zig Zag flow

    i = 999
    j = 999
    i_anchor = 999
    j_anchor = 999

    while i > 99 and j > 99:
        if palindrome(i*j):
            return i*j
        if i == 999 or j == 100:
            if i_anchor == j_anchor:
                j_anchor = j_anchor - 1
            else:
                i_anchor = i_anchor - 1
            i = i_anchor
            j = j_anchor
        else:
            #Go up right
            i = i + 1
            j = j - 1
        
    
        
