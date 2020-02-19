import itertools
import random
from itertools import *

kleurenList = ["r", "g", "b", "y", "w", "p"] # dit is een lijst met alle kleuren

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

def generateFirstTurn():
    colorString = []
    while True:
        for i in range(0, 4):
            colorString.append(random.choice(kleurenList))
        if colorString[0] == colorString[1] and colorString[2] == colorString[3] and colorString[0] != colorString[2]:
            break
        elif colorString[0] == colorString[2] and colorString[1] == colorString[3] and colorString[0] != colorString[1]:
            break
        elif colorString[0] == colorString[3] and colorString[1] == colorString[2] and colorString[0] != colorString[1]:
            break
        else:
            colorString.clear()
    return colorString


def kleurenInCombo(combo):
    kleuren = list(dict.fromkeys(combo))
    return kleuren

def generateFeedback(kleurstring, key):
    """Computer geeft feedback op de opgeleverde codecombo, vergelijkt met 2e combo. Return is ZWART, WIT"""
    tempkleurstring = kleurstring.copy()    # 4x red
    tempcolorkey = key.copy()               # b y y r
    zwart = 0
    wit = 0
    print(tempkleurstring)
    print(tempcolorkey)
    for i in range(0, len(tempkleurstring)):
        if tempkleurstring[i] in tempcolorkey:
            kleur = tempkleurstring[i]
            print(i)
            print(kleur)
            print(tempcolorkey[i])

            if tempkleurstring.index(kleur) == tempcolorkey.index(kleur):
                print("gaat dit af")
                # print("Value {} is op de juiste plek".format(i))
                tempcolorkey[(tempcolorkey.index(kleur))], tempkleurstring[(tempkleurstring.index(kleur))] = "z-pin"
                zwart += 1
            else:
                # print("Value {} staat in de lijst, niet op juiste plek".format(i))
                tempkleurstring[(tempkleurstring.index(kleur))] = "w-pin"
                tempcolorkey[(tempcolorkey.index(kleurstring[i]))] = "w-pin"
                wit += 1
    print(tempkleurstring)
    print(tempcolorkey)
    return zwart, wit


def generateFeedback2(kleurstring, key):
    """Computer geeft feedback op de opgeleverde codecombo, vergelijkt met 2e combo. Return is ZWART, WIT"""
    tempkleurstring = kleurstring.copy()    # 4x red
    tempcolorkey = key.copy()               # b y y r
    zwart = 0
    wit = 0
    for i in range(0, len(tempkleurstring)):
        if tempkleurstring[i] == tempcolorkey[i]:
            # print("Value {} is op de juiste plek".format(i))
            tempcolorkey[i] = "z-pin ck"
            tempkleurstring[i] = "z-pin ks"
            zwart += 1
    for i in range(0, len(tempkleurstring)):
        if tempkleurstring[i] in tempcolorkey:
            tempcolorkey[(tempcolorkey.index(tempkleurstring[i]))] = "w-pin"
            tempkleurstring[i] = "w-pin"
            wit += 1
    return zwart, wit

# fibr(9)
# combo3()
# print(generateFirstTurn())
# print(kleurenInCombo(["r", "g", "r", "b"]))
print(generateFeedback2(["r", "p", "b", "r"], ["b", "y", "p", "r"]))