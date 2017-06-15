# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Pandigital Multiples

# this one is fairly easy to do, just iterate

def isdup(n, arr=[0,0,0,0,0,0,0,0,0,0]):
    # Take a number and see if any digits duplicated
    s = str(n)
    a = list(arr)
    #Time saving check
    if "0" in s:
        return (True,a)
    for c in s:
        i = int(c)
        if a[i] > 0:
            return (True,a)
        else:
            a[i] = 1

    return (False,a)

def digitcount(arr):
    for i in range(1,10):
        if arr[i] != 1:
            return False
    return True

def pandigital(i):
    # Returns true if there is some n for which i * (1...n) produces a concatenated pandigital number 1..9

    (b,arr) = isdup(i)
    if b:
        return False

    for n in range(2,9):
        (b,arr) = isdup(i*n,arr)
        if b:
            return False
        if digitcount(arr):
            return True

    return True

def pandagen(i):
    # Assumes that it is a pandigital ready number
    # Just generates the number

    s = ""
    for n in range(1,9):
        if len(s) == 9:
            return s
        s += (str(n*i))

    return s

def problem38():
    curr_win = ""
    for i in range(1,10000): #Can't be more than this as 9 digits so has to be a 4 digit number max
        if pandigital(i):
            s = pandagen(i)
            print(s)
            if s > curr_win:
                curr_win = s
                

    return curr_win
        
    
    
    
