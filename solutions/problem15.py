# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Lattice Paths
# Fairly Interesting problem

size = 20

memory = {}

def latticex(i,j):
    x = memory.get(str(i)+","+str(j))
    if x is None:
        y = lattice(i,j,0)
        memory[str(i)+","+str(j)] = y
        return y
    else:
        return int(x)

def lattice(i,j,solutions):
    
    if i == size and j == size:
        return solutions+1
    if i > size or j > size:
        return 0
    a = latticex(i,j+1)
    b = latticex(i+1,j)
    return solutions+a+b

for i in range(size,0,-1):
    for j in range(size,0,-1):
        print(str(i)+","+str(j))
        latticex(i,j)

print(latticex(0,0))
