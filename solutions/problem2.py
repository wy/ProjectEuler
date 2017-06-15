# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

def problem2():
	i = 1
	j = 2
	acc = 0
	
	while j <= 4000000:
		if j % 2 == 0:
			acc = acc + j
		k = i + j
		i = j
		j = k
	return acc
