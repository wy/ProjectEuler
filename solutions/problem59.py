# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017
# XOR decryption

# a ^ b does xor

def problem59():
    with open('../helperfiles/p059_cipher.txt', 'r') as f:
        data = f.readline()
    encrypted = data.split(",")
    print(encrypted)
    s=""
    max = 0
    maxi = 0

    lowercase = range(97,122)
    code = []

    for i in lowercase:
        c = 0
        tot = 0
        for e in range(0,len(encrypted),3):
            tot += 1
            o = i ^ int(encrypted[e])
            if o in range(65,123)  or o == 32:
                c += 1

        if c > max:
            max = c
            maxi = i
    code.append(maxi)

    max = 0
    maxi = 0

    for i in lowercase:
        c = 0
        tot = 0
        for e in range(1,len(encrypted),3):
            tot += 1
            o = i ^ int(encrypted[e])
            if o in range(65,123)  or o == 32:
                c += 1
        if c > max:
                max = c
                maxi = i
    code.append(maxi)

    max = 0
    maxi = 0

    for i in lowercase:
        c = 0
        tot = 0
        for e in range(2,len(encrypted),3):
            tot += 1
            o = i ^ int(encrypted[e])
            if o in range(65,123) or o == 32:
                c += 1
        if c > max:
                max = c
                maxi = i
    code.append(maxi)

    score = 0
    for e in range(0,len(encrypted),3):
        s += chr(code[0] ^ int(encrypted[e]))
        score += code[0] ^ int(encrypted[e])
        if e+1 < len(encrypted):
            s += chr(code[1] ^ int(encrypted[e+1]))
            score += code[1] ^ int(encrypted[e + 1])
        if e + 2 < len(encrypted):
            s += chr(code[2] ^ int(encrypted[e+2]))
            score += code[2] ^ int(encrypted[e + 2])

    return score

print(problem59())
