# coding: utf8
# Author: Wing Yung Chan (~wy)
# Date: 2017
# Poker Hands

class PokerCard(object):

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


    def getValue(self):
        return self.value

    def getValueNumeric(self):
        v = self.value
        if v == '2':
            return 2
        if v == '3':
            return 3
        if v == '4':
            return 4
        if v == '5':
            return 5
        if v == '6':
            return 6
        if v == '7':
            return 7
        if v == '8':
            return 8
        if v == '9':
            return 9
        if v == 'T':
            return 10
        if v == 'J':
            return 11
        if v == 'Q':
            return 12
        if v == 'K':
            return 13
        if v == 'A':
            return 14

    def getSuit(self):
        return self.suit

class PokerHand(object):

    def __init__(self):
        self.cards = []

    def addCard(self,pokercard):
        self.cards.append(pokercard)

    def HighCard(self):
        # Returns the values in order
        values = []
        for c in self.cards:
            values.append(c.getValueNumeric())
        values.sort(reverse=True)

        return values

    def OnePair(self):
        # Returns None if no matching pair
        # Otherwise it returns an array of comparable value
        # i.e. the pair, then the sequence of highest cards
        # This assumes there aren't triples, 2-pairs etc

        pair = 0
        values = []
        for i in range(0,len(self.cards)):
            c = self.cards[i]
            for j in range(i+1,len(self.cards)):
                c2 = self.cards[j]
                if c.getValueNumeric() == c2.getValueNumeric():
                    # Found a pair
                    pair = c.getValueNumeric()
                    for k in range(0,len(self.cards)):
                        if k != i and k != j:
                            values.append(self.cards[k].getValueNumeric())
                    break
        values.sort(reverse=True)

        if pair == 0:
            return None
        result = [pair]
        for i in values:
            result.append(i)
        return result

    def TwoPair(self):
        # Returns None if no matching pair
        # Otherwise it returns an array of comparable value
        # i.e. the top pair, then the second top pair, then the sequence of highest cards
        # This assumes there aren't better hand combos

        pair1 = 0
        pair2 = 0
        v = 0
        for i in range(0,len(self.cards)):
            c = self.cards[i]
            for j in range(i+1,len(self.cards)):
                c2 = self.cards[j]
                if c.getValueNumeric() == c2.getValueNumeric():
                    # Found a pair
                    pair1 = c.getValueNumeric()
                    for k in range(0,len(self.cards)):
                        if k != i and k != j:
                            c3 = self.cards[k]
                            for m in range(k+1,len(self.cards)):
                                if m != i and m != j:
                                    c4 = self.cards[m]
                                    if c3.getValueNumeric() == c4.getValueNumeric():
                                        # Found another pair
                                        pair2 = c3.getValueNumeric()
                                        for n in range(0, len(self.cards)):
                                            if n != i and n != j and n != k and n != m:
                                                v = self.cards[n].getValueNumeric()
                                        break

        if pair1 == 0 or pair2 == 0:
            return None
        if pair1 > pair2:
            return [pair1,pair2,v]
        else:
            return [pair2,pair1,v]

    def ThreeOfAKind(self):
        # Returns None if no matching three of a kind
        # Otherwise it returns an array of comparable value
        # i.e. the three of a ind, then the sequence of highest cards
        # This assumes there aren't beating hands

        threes = 0
        values = []
        for i in range(0,len(self.cards)):
            c = self.cards[i]
            for j in range(i+1,len(self.cards)):
                c2 = self.cards[j]
                if c.getValueNumeric() == c2.getValueNumeric():
                    # Found a pair
                    pair = c.getValueNumeric()
                    for k in range(j+1,len(self.cards)):
                        c3 = self.cards[k]
                        if c3.getValueNumeric() == c2.getValueNumeric():
                            # Found the triplet
                            threes = c3.getValueNumeric()
                            for m in range(0, len(self.cards)):
                                if m != i and m != j and m != k:
                                    values.append(self.cards[m].getValueNumeric())
                    break
        values.sort(reverse=True)

        if threes == 0:
            return None
        result = [threes]
        for i in values:
            result.append(i)
        return result

    def Straight(self):

        values = []
        for c in self.cards:
            values.append(c.getValueNumeric())
        values.sort(reverse=True)
        for i in range(1,5):
            if values[i] != (values[i-1]-1):
                return None
        return [values[0]] # Top Value as sorted descending

    def Flush(self):
        suit = 'A'
        for c in self.cards:
            if suit == 'A':
                suit = c.getSuit()
            elif suit != c.getSuit():
                return None

        # So it's a Flush, return the values
        values = []
        for c in self.cards:
            values.append(c.getValueNumeric())
        values.sort(reverse=True)
        return values

    def FullHouse(self):
        res = self.ThreeOfAKind()
        if res == None:
            return None
        if res[1]==res[2]:
            return res
        return None

    def FourOfAKind(self):
        # Returns None if no matching four of a kind
        # Otherwise it returns an array of comparable value
        # i.e. the four of a kind, then the highest remaining card
        # This assumes there aren't beating hands

        fours = 0
        v = 0
        for i in range(0,len(self.cards)):
            c = self.cards[i]
            for j in range(i+1,len(self.cards)):
                c2 = self.cards[j]
                if c.getValueNumeric() == c2.getValueNumeric():
                    # Found a pair
                    pair = c.getValueNumeric()
                    for k in range(j+1,len(self.cards)):
                        c3 = self.cards[k]
                        if c3.getValueNumeric() == c2.getValueNumeric():
                            # Found the triplet
                            for m in range(k+1,len(self.cards)):
                                c4 = self.cards[m]
                                if c4.getValueNumeric() == c3.getValueNumeric():
                                    # Found the four
                                    fours = c4.getValueNumeric()
                                    for n in range(0, len(self.cards)):
                                        if n != i and n != j and n != k and n != m:
                                            v = self.cards[n].getValueNumeric()
                                        break

        if fours == 0:
            return None
        return [fours,v]

    def StraightFlush(self):
        if self.Flush() != None:
            v = self.Straight()
            if v != None:
                return [v] # Top Card
        return None

    def RoyalFlush(self):
        v = self.StraightFlush()
        if v is None:
            return None
        if v == 14:
            return [v]
        return None

    def HighestHand(self):

        r = self.RoyalFlush()
        if r is not None:
            return (10,r)
        r = self.StraightFlush()
        if r is not None:
            return (9,r)
        r = self.FourOfAKind()
        if r is not None:
            return (8,r)
        r = self.FullHouse()
        if r is not None:
            return (7,r)
        r = self.Flush()
        if r is not None:
            return(6,r)
        r = self.Straight()
        if r is not None:
            return (5,r)
        r = self.ThreeOfAKind()
        if r is not None:
            return (4,r)
        r = self.TwoPair()
        if r is not None:
            return (3,r)
        r = self.OnePair()
        if r is not None:
            return (2,r)
        r = self.HighCard()
        return (1,r)

def compareHands(H1,H2):
    (s1,r1) = H1.HighestHand()
    (s2,r2) = H2.HighestHand()
    if s1 > s2 :
        return 1
    if s1 < s2 :
        return 2

    # s1 == s2 so need to compare r1 and r2

    for i in range(0,len(r1)):
        if r1[i] > r2[i]:
            return 1
        if r1[i] < r2[i]:
            return 2
    print("Something went wrong")
    return None # impossible

def parseLine(line):
    cards = line.split()
    H1 = PokerHand()
    H2 = PokerHand()
    for i in range(0,5):
        c = cards[i]
        v = c[0]
        s = c[1]
        card = PokerCard(v,s)
        H1.addCard(card)
    for i in range(5, 10):
        c = cards[i]
        v = c[0]
        s = c[1]
        card = PokerCard(v, s)
        H2.addCard(card)
    return compareHands(H1,H2)

#print(parseLine("8C TS KC 9H 4S 7D 2S 5D 3S AC"))
#print(parseLine("2D 9C AS AH AC 3D 6D 7D TD QD"))
#print(parseLine("4D 6S 9H QH QC 3D 6D 7H QD QS"))

def problem54():
    cnt = 0
    with open('../helperfiles/p054_poker.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            winner = parseLine(line)
            if winner == 1:
                cnt += 1

    return cnt

print(problem54())