# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

# Triangle Sums

triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

triangle_lines = triangle.split("\n")

triangle_arr = []

for line in triangle_lines:
    arr = line.split()
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    triangle_arr.append(arr)


size = 14

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
    if i == 14:
        return summary + triangle_arr[i][j]
    a = tri_sumx(i+1,j)
    b = tri_sumx(i+1,j+1)
    return max(a,b)+triangle_arr[i][j]
    
for i in range(14,-1,-1):
    for j in range(i,-1,-1):
        tri_sumx(i,j)

    


    
