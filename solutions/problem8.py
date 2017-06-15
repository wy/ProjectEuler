# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

def problem8(n):

    s = str(n)
    i = 0
    lastmax = 0
    
    
    while i <= len(s)-13:
        acc = 1
        move = i
        #optimisation
        for j in range(i,i+13):
            if int(s[j]) == 0:
                move = j+1
        if move == i:
            for k in range(i,i+13):
                acc = acc * int(s[k])
        if acc > lastmax:
            lastmax = acc
        i = i + 1

    return lastmax
        
