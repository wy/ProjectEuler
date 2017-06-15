# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017

from datetime import date, timedelta

start = date(1900, 1, 1)
end = date(2000, 12, 31)

i = 0
dt = start
acc = 0
while i < 36899:
    if i % 7 == 6 and dt.day==1 and dt.year > 1900:
        # It's a Sunday and first of the month
        acc = acc + 1
        
    dt = dt + timedelta(days=1)
    i = i + 1

print(acc)
