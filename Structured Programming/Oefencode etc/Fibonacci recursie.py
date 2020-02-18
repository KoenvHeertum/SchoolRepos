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

# fibr(9)
combo3()