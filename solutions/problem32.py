# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Lazy Solution

def problem32():
    answers = set()
    for i in range(2,1000):
        for j in range(i+1,10000):
            p = i * j
           
            x = str(p)+str(i)+str(j)
            if len(x) != 9 or '0' in x or '9' not in x or '1' not in x or '2' not in x or '3' not in x or '4' not in x or '5' not in x or '6' not in x:
                continue
            
            arr = []
            for a in x:
                arr.append(a)
            arr.sort()
            res = "".join(arr)
            if res == "123456789":
                print(p,i,j)
                answers.add(p)
    acc = 0
    for x in answers:
        acc += x
    print(acc)
            
problem32()
