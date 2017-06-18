# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Coded Triangle Numbers
# Try and be smart and generate triangle numbers only when needed

import string
di=dict(zip(string.ascii_letters,[ord(c)%32 for c in string.ascii_letters]))

def getscore(word):
    # Numeric Score based on summing the Alphabet Scores of each letter
    score = 0
    for s in word:

        score += di[s]
    return score

def istriangle(word,triangle_arr):
    score = getscore(word)
    while score > triangle_arr[-1]:
        n = 1 + len(triangle_arr)
        triangle_arr.append((n*(n+1))//2)

    return score in triangle_arr
        

def problem42():
    triangle_arr = [1]
    cnt = 0
    line = ""

    with open('../helperfiles/p042_words.txt','r') as f:
        line = f.readline()

    words = line.replace('"','').split(",")

    for w in words:
        if istriangle(w, triangle_arr):
            cnt += 1
            print(w)

    return cnt

print(problem42())

