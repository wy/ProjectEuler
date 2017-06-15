# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Integer Right Triangles

# Find p <= 1000 with the most solutions of integer right angle triangles
import math

def solutions(p):
    cnt = 0
    for i in range(1,p-2):
        for j in range(i+1,p-2-i):
            k = math.sqrt(i*i + j*j)
            if math.floor(k) == math.ceil(k) and i + j + k == p:
                # solution!
                cnt += 1
                #print(i,j,k)

    return cnt

def problem39():
    cmax = 0
    pmax = 0
    for p in range(1,1001):
        m = solutions(p)
        if m > cmax:
            cmax = m
            pmax = p

    return pmax
