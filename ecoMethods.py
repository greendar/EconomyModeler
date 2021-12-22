import random as r
from ecoDat import *

class Person:
    def __init__(self):
        self.name = self.getName()

    def getName(self):
        notDone = True
        while notDone:
            const = "bcdfghjklmnpqrstvwxyz"
            vowel = "aeiou"
            nameOut = r.choice(const).upper() + r.choice(vowel) + r.choice(const)
            if nameOut not in badNames:
                notDone = False
        return nameOut


class Buyer(Person):
    def __init__(self):
        self.name = self.getName()
        self.maxPrice = r.randint(1, 10)


class Seller(Person):
    def __init__(self):
        self.name = self.getName()
        self.minPrice = r.randint(1, 10)


class AllSellers:
    numSellers = 10

    def __init__(self):
        self.sellers = sellerList()

    def sellerList():
        listOut = []
        for i in range(numSellers):
            listOut.append(Seller())


class AllBuyers:
    numBuyers = 10

    def buyerList():
        listOut = []
        for i in range(numBuyers):
            listOut.append(Buyer())



if __name__ == "__main__":
    sellerList()
    buyerList()
    print(sellerList)
    print(buyerList)
