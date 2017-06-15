# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Use solution to problem 18

triangle_arr = []

with open('../helperfiles/p067_triangle.txt','r') as f:
    for line in f:
        arr = line.split()
        for i in range(len(arr)):
            arr[i] = int(arr[i])
        triangle_arr.append(arr)


size = len(triangle_arr)-1

memory = {}

def tri_sumx(i,j):
    x = memory.get(str(i)+","+str(j))
    if x is None:
        answer = tri_sum(i,j,0)
        memory[str(i)+","+str(j)]= answer
        return answer
    else:
        return memory.get(str(i)+","+str(j))

def tri_sum(i,j,summary):
    if i == size:
        return summary + triangle_arr[i][j]
    a = tri_sumx(i+1,j)
    b = tri_sumx(i+1,j+1)
    return max(a,b)+triangle_arr[i][j]
    
for i in range(size,-1,-1):
    for j in range(i,-1,-1):
        tri_sumx(i,j)


