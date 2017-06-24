# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017
# Prime Digit Replacements

# This is actually quite hard to think about an optimal solution

# Upgraded faster prime test
def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w

    return True

def primegenerator():
    primearr = [2]
    max = 1000000
    for i in range(100001,max,2):
        if prime(i):
            primearr.append(i)

    return primearr



def test(prime, multiplier, primearr):
    score = 1

    variants = prime
    answers = [prime]
    s = str(multiplier)
    strp = str(prime)
    cnt = 0

    # Test that the digits are identical to start with
    iden = 'A'
    for m in range(0,len(s)):
        if s[m] == '1':
            x = strp[m + len(strp) - len(s)]
            if iden == 'A':
                iden = x
            elif x != iden:
                return False
    for j in s:
        if j == '1':
            cnt += 1
            # only cnt many digits can change
    for i in range(1,10):
        variants += multiplier
        if len(str(variants)) > len(str(prime)):
            break
        strv = str(variants)
        c = 0
        for k in range(0, len(strp)):
            if strv[k] != strp[k]:
                c += 1
        if c > cnt:
            break
        if variants in primearr:
            score += 1
            answers.append(variants)

    if score == 8:
        print(multiplier, answers)
    return score==8

def quicktest(prime):
    s = str(prime)
    cnt = 0
    for x in s[:-1]:
        if int(x) <= 2:
            cnt += 1
    return cnt == 0

def problem51():
    primearr = primegenerator()
    length = len(primearr)
    for i in range(0,length):
        p = primearr[i]
        if quicktest(p):
            continue
        print(p)
        if p < 10:
            continue
        s = test(p,10,primearr)
        if s:
            return p
        if p > 100:
            s = test(p,110,primearr)
            if s:
                return p
            s = test(p,100,primearr)
            if s:
                return p
        if p > 1000:
            s = test(p,1110,primearr)
            if s:
                return p
            s = test(p,1100,primearr)
            if s:
                return p
            s = test(p,1000, primearr)
            if s:
                return p
            s = test(p,1010, primearr)
            if s:
                return p
        if p > 10000:
            s = test(p,11110,primearr)
            if s:
                return p
            s = test(p,11100,primearr)
            if s:
                return p
            s = test(p,11000, primearr)
            if s:
                return p
            s = test(p,10000, primearr)
            if s:
                return p
            s = test(p,10010, primearr)
            if s:
                return p
            s = test(p,10110, primearr)
            if s:
                return p
            s = test(p,11010, primearr)
            if s:
                return p
            s = test(p, 10100, primearr)
            if s:
                return p
        if p > 100000:
            s = test(p, 111110, primearr)
            if s:
                return p
            s = test(p, 111100, primearr)
            if s:
                return p
            s = test(p, 111000, primearr)
            if s:
                return p
            s = test(p, 110000, primearr)
            if s:
                return p
            s = test(p, 110010, primearr)
            if s:
                return p
            s = test(p, 110110, primearr)
            if s:
                return p
            s = test(p, 111010, primearr)
            if s:
                return p
            s = test(p, 110100, primearr)
            if s:
                return p
            s = test(p, 100010, primearr)
            if s:
                return p
            s = test(p, 100110, primearr)
            if s:
                return p
            s = test(p, 101110, primearr)
            if s:
                return p
            s = test(p, 100100, primearr)
            if s:
                return p
            s = test(p, 101000, primearr)
            if s:
                return p
            s = test(p, 101100, primearr)
            if s:
                return p
            s = test(p, 101110, primearr)
            if s:
                return p
            s = test(p, 101010, primearr)
            if s:
                return p

#test(56003,110,[56003, 56113, 56333, 56443, 56663, 56773, 56993])

print(problem51())

