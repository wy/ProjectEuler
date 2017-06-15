# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Number Letter Counts
# Some of the digits are not easily generated so just state them
# Rest can be

dict_tens = {0 : -3,
          1 : 3,
          2 : 3,
          3 : 5,
          4 : 4,
          5 : 4,
          6 : 3,
          7 : 5,
          8 : 5,
          9 : 4,
          10 : 3,
          11 : 6,
        12 : 6,
            13 : 8,
             14 : 8,
             15 : 7,
             16 : 7,
             17 : 9,
             18 : 8,
             19 : 8,
             20 : 6,
             30 : 6,
             40 : 5,
             50 : 5,
             60 : 5,
             70 : 7,
             80 : 6,
             90 : 6
    
    }

for i in range(21,100):
    if i % 10 != 0:
        j = i // 10
        k = i % 10
        dict_tens[i] = dict_tens[10*j]+dict_tens[k]

def wordcount(x):
    if x == 1000:
        return 11
    if x < 100:
        return dict_tens[x]
    else:
        j = int(str(x)[0])
        k = int(str(x)[-2:])
        return dict_tens[j] + 10 + dict_tens[k]

acc = 0
for i in range(1,1001):
    acc = acc + wordcount(i)

print(acc)



    
