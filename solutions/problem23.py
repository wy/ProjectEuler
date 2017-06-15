# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

#non-abundant sums

# N is non-abundant if the sum of its proper divisors is <= N
# prop(N) = Set{1 <= i < N | N % i == 0}


def properdivisors(N):
    acc = 0

    for i in range(1,N):
        if N % i == 0:
            acc = acc + i

    return acc

def abundant(N):
    return properdivisors(N) > N

def generateA():
    AList = []
    for i in range(1, 28124):
        if abundant(i):
            AList.append(i)

    return AList

def generateAPairs(AList):
    APairs = set()
    for i in AList:
        for j in AList:
            if i+j <= 28123
            APairs.add(i+j)
    return APairs


def problem23():
    acc = 0
    APairs = generateAPairs(generateA())
    for i in range(1, 28124):
        if i not in APairs:
            acc = acc + i

    return acc

    
