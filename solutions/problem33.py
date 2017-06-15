# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Digit Cancelling Fractions
# Looking for ab/cd = x/y where (a,b) and (c,d) share a common number and (x,y) is what happens when you remove it
from fractions import Fraction

def problem33():
    fcum = Fraction(1)
    for i in range(10,100):
        for j in range(i+1,100):
            si = str(i)
            sj = str(j)
            f = Fraction(i,j)
            if f.numerator > 9 or f.denominator > 9:
                continue
            if si[1]==sj[1] and si[1] == "0":
                continue
            if si[0] ==  sj[1] and int(sj[0]) > 0 and Fraction(int(si[1]),int(sj[0])) == f:
                print((i,j,f))
                fcum *= f
            elif si[1] ==  sj[1] and int(sj[0]) > 0 and Fraction(int(si[0]),int(sj[0])) == f:
                print((i,j,f))
                fcum *= f
            elif si[0] ==  sj[0] and int(sj[1]) > 0 and Fraction(int(si[1]),int(sj[1])) == f:
                print((i,j,f))
                fcum *= f
            elif si[1] ==  sj[0] and int(sj[1]) > 0 and Fraction(int(si[0]),int(sj[1])) == f:
                print((i,j,f))
                fcum *= f

    return fcum
            
