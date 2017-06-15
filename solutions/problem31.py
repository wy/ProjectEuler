# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Coin Sums
# 1,2,5,10,20,100,200

# This is all about generating possible solutions from bottom up
# And then memoising it to avoid recalculations

answers = {}

def makeup(n,maxcoin):
    x = answers.get((n,maxcoin))
    if x is None:
        if n >= 200 and maxcoin >= 200:
            a200 = makeup(n-200,200)
            a100 = makeup(n-100,100)
            a50 = makeup(n-50,50)
            a20 = makeup(n-20,20)
            a10 = makeup(n-10,10)
            a5 = makeup(n-5,5)
            a2 = makeup(n-2,2)
            a1 = makeup(n-1,1)
            answers[(n,maxcoin)] = a200 + a100+ a50 + a20 + a10 + a5 + a2 + a1
            return answers[(n,maxcoin)]
        elif n >= 100 and maxcoin >= 100:
            a100 = makeup(n-100,100)
            a50 = makeup(n-50,50)
            a20 = makeup(n-20,20)
            a10 = makeup(n-10,10)
            a5 = makeup(n-5,5)
            a2 = makeup(n-2,2)
            a1 = makeup(n-1,1)
            answers[(n,maxcoin)] = a100+ a50 + a20 + a10 + a5 + a2 + a1
            return  answers[(n,maxcoin)]
        elif n >= 50 and maxcoin >= 50:
            a50 = makeup(n-50,50)
            a20 = makeup(n-20,20)
            a10 = makeup(n-10,10)
            a5 = makeup(n-5,5)
            a2 = makeup(n-2,2)
            a1 = makeup(n-1,1)
            answers[(n,maxcoin)] = a50 + a20 + a10 + a5 + a2 + a1       
            return answers[(n,maxcoin)]                       
        elif n >= 20 and maxcoin >= 20:
            a20 = makeup(n-20,20)
            a10 = makeup(n-10,10)
            a5 = makeup(n-5,5)
            a2 = makeup(n-2,2)
            a1 = makeup(n-1,1)
            answers[(n,maxcoin)] = a20 + a10 + a5 + a2 + a1
            return answers[(n,maxcoin)]
        elif n >= 10 and maxcoin>=10:
            a10 = makeup(n-10,10)
            a5 = makeup(n-5,5)
            a2 = makeup(n-2,2)
            a1 = makeup(n-1,1)
            answers[(n,maxcoin)] = a10 + a5 + a2 + a1
            return answers[(n,maxcoin)]
        elif n >= 5 and maxcoin >= 5:
            a5 = makeup(n-5,5)
            a2 = makeup(n-2,2)
            a1 = makeup(n-1,1)
            answers[(n,maxcoin)] = a5 + a2 + a1
            return answers[(n,maxcoin)]
        elif n >= 2 and maxcoin >= 2:
            a2 = makeup(n-2,2)
            a1 = makeup(n-1,1)
            answers[(n,maxcoin)] = a2 + a1
            return answers[(n,maxcoin)]
        elif n >= 1 and maxcoin >= 1:
            a1 = makeup(n-1,1)
            answers[(n,maxcoin)]= a1
            return answers[(n,maxcoin)]
        elif n == 0:
            return 1
        else:
            return 0
    else:
        return x
    
