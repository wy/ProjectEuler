# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Coded Triangle Numbers
# Try and be smart and generate triangle numbers only when needed


import string
di=dict(zip(string.ascii_letters,[ord(c)%32 for c in string.ascii_letters]))

def istriangle(word,triangle_arr):
    score = getscore(word)
    while score > triangle_arr[-1]
        n = 1 + len(triangle_arr)
        triangle_arr.append((n*(n+1))//2)

    return score in triangle_arr
        

def problem42():
    triangle_arr = [1]
    cnt = 0
    with open('../helperfiles/p042_words.txt','r') as f:
        for line in f:
            if istriangle(line,triangle_arr):
                cnt += 1
                print(line)
    
