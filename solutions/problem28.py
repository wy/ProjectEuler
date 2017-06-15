# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Number Spiral Diagonals
# Simple solution is to generate the 1001 x 1001 grid
# And then to sum the diagonals

def sumdiagonals(matrix):
    acc = 0
    for i in range(0, len(matrix)):
        acc += matrix[i][i]
        acc += matrix[len(matrix)-i-1][i]
    return acc-1 # double count the centre so remove that one

def spiralGenerator(n):
    # create a n x n array
    assert n%2==1
    matrix = []
    for i in range(0,n):
        arr = []
        for j in range(0,n):
            arr.append(0)
        matrix.append(arr)

    
    i = n//2
    j = n//2
    direction = (0,1)
    amount = 1
    remaining = 1
    acc = 1
    while i != 0 or j != n:
        
        matrix[i][j] = acc        
        acc += 1
        if remaining > 0:
            i += direction[0]
            j += direction[1]
            remaining -= 1
        if remaining == 0:
            if direction == (0,1):
                direction = (1,0)
            elif direction == (1,0):
                direction = (0,-1)
                amount += 1
            elif direction == (0,-1):
                direction = (-1,0)
            elif direction == (-1,0):
                direction = (0,1)
                amount+=1
            remaining = amount


    return matrix

def problem28():
    matrix = spiralGenerator(1001)
    return sumdiagonals(matrix)
