# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017
# Prime Pair Sets
# A set of primes {p} is a prime pair set if each pair of primes can be concatenated in any order and form a prime
# Goal: find the set of 5 primes that has minimal sum and forms a prime pair set

# All we need to do is find all the pairs and look at finding a clique


# Upgraded faster prime test
def prime(n : int) -> bool:
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

def primelist(n : int):
    # return list of first n primes
    primes = [2]
    j = 3
    for i in range(0,n):
        if prime(j):
            primes.append(j)
        j+=2
    print(primes[-1])
    return primes

def generatepairs(primes):
    # return list of primes for each prime
    pairs = {p : [] for p in primes}
    max = primes[-1]
    for i in primes:
        cnt = 0
        for j in primes:
            if i >= j:
                continue
            x1 = int(str(i)+str(j))
            x2 = int(str(j)+str(i))
            if (x1 > max and prime(x1)) or (x1 <= max and x1 in primes):
                if (x2 > max and prime(x2)) or (x2 <= max and x2 in primes):
                    pairs.get(i).append(j)
                    pairs.get(j).append(i)
                    cnt += 1
        if cnt == 0:
            del pairs[i]


    return pairs

def pruning(pairs, minimum):

    change = 1
    while(change > 0):
        change = 0
        print(len(pairs))
        for p in list(pairs.keys()):
            if len(pairs.get(p)) < minimum:
                del pairs[p]
                change = 1
            else:
                twins = pairs.get(p)
                newlist = []
                for t in twins:
                    if t in list(pairs.keys()):
                        newlist.append(t)
                    else:
                        change = 1
                pairs[p] = newlist

    return pairs

def pruneV2(pairs, minimum):
    # Next step of pruning
    change = 1
    while change > 0 :
        change = 0
        print(len(pairs))
        for p in list(pairs.keys()):
            # e.g. p = 3
            v = pairs.get(p) #list for 3 e.g. 7,31,37,73

            anymatches = 0
            newlist = []
            for x in v:
                # e.g. x = 7
                if x not in list(pairs.keys()): # deal with case of deletion during loop
                    continue
                v2 = pairs.get(x) #list for 7. e.g 3,19,61,67

                matches = 2 # naturally x and p match already
                for a in v:
                    for b in v2:
                        if a == b:
                            matches += 1
                if matches >= minimum+1:
                    anymatches += 1
                    newlist.append(x)

            pairs[p] = newlist

            if anymatches == 0:
                # prune
                del pairs[p] # since none of its pairs has enough in common
                change = 1
    return(pairs)

x = generatepairs(primelist(5000))
for  _ in range(0,10):
    pairs = pruning(x,4)
    pairs = pruneV2(x,4)
    print(pairs)
