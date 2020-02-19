import itertools
from itertools import *


def fibr(n):
    if n < 2:
        return 1
    return fibr(n-1) + fibr(n-2)

def combo():
    comb = combinations_with_replacement([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6], 4)
    counter = 0
    for i in list(comb):
        print(i)
        counter += 1
        print(counter)
#     1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6

def combo2():
    algstr = []
    list = [1,2,3]
    list2 = list.copy()
    list3 = list.copy()
    for i in list:
        algstr.append(i)
        for j in list2:
            algstr.append(j)
            for k in list3:
                algstr.append(k)
                print(algstr)
                algstr.pop(-1)
            algstr.pop(-2)
        algstr.pop(-3)

def combo3():
    allCombinations = list(combinations_with_replacement(["r", "g", "b", "y", "w", "p", "r", "g", "b", "y", "w", "p", "r", "g", "b", "y", "w", "p", "r", "g", "b", "y", "w", "p"], 4))
    counter = 0
    for i in allCombinations:
        print(list(i))
        counter += 1
        print(counter)

def generateFeedback(kleurstring, key):
    """Computer geeft feedback op de opgeleverde codecombo, vergelijkt met 2e combo. Return is ZWART, WIT"""
    tempcolorkey = key.copy()
    zwart = 0
    wit = 0
    for i in range(0, len(kleurstring)):
        if kleurstring[i] in tempcolorkey:
            if kleurstring[i] == tempcolorkey[i]:
                # print("Value {} is op de juiste plek".format(i))
                tempcolorkey[i] = "z-pin"
                zwart += 1
            else:
                # print("Value {} staat in de lijst, niet op juiste plek".format(i))
                tempcolorkey[(tempcolorkey.index(kleurstring[i]))] = "w-pin"
                wit += 1
    print(tempcolorkey)
    return zwart, wit

# fibr(9)
# combo3()
print(generateFeedback(['w', 'r', 'g', 'r'], ['r', 'r', 'r', 'r']))