# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

import string
di=dict(zip(string.ascii_letters,[ord(c)%32 for c in string.ascii_letters]))


with open("../helperfiles/p022_names.txt") as f:
    content = f.readlines()

names = content[0].replace('"','').lower().split(",")

names.sort()

def score(s):
    acc = 0
    for i in s:
        acc = acc + di[i]

    return acc

rank = 1
acc = 0
for name in names:
    acc = acc + (score(name) * rank)
    rank = rank + 1

print(acc)
