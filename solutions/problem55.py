# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017
# Lychrel Numbers

# Iterate step : take a number n and add on rev(n) which is n with its digits reversed
# stop when n+rev(n) is palindrome

def reverse(n : int) -> int:
    s = str(n)
    rStr = s[::-1]
    return int(rStr)

def palindrome(n : int) -> bool:
    return reverse(n) == n

def lychrel(n):
    # Iterate up to 50 times
    i = 0
    while (i < 50):
        i += 1
        r = reverse(n)
        p = r + n
        if palindrome(p):
            return False
        n = p
    return True

def problem55():
    cnt = 0
    for i in range(1,10000):
        if lychrel(i):
            cnt += 1

    return cnt

print(problem55())