# Opdracht 3
def count(list):
    numberdict = {}
    for number in list:
        if number in numberdict:
            numberdict[number] += 1
        else:
            numberdict[number] = 1
    return numberdict

def difference(list):
    list.sort()
    maxDifference = 0
    difference = 0
    for item in range(1, len(list)):
        difference = list[item] - list[item-1]
        if difference > maxDifference:
            maxDifference = difference
    print("{} is max diff".format(maxDifference))

def listChecker(list):
    dict = count(list)
    zeroes = 0
    ones = 0
    for i in dict.values():
        if i == 0:
            zeroes += 1
        elif i == 1:
            ones += 1
        else:
            print("Dat is geen 0 of 1.")
            break
    print("{} zeroes, {} ones".format(zeroes, ones))
    if ones > zeroes:
        print("Meer ones dan zeroes")
    if zeroes > 12:
        print("Te veel zeroes, helaas")




print(count([1, 1, 2, 2, 2, 3, 4, 5, 5, 5, 6]))
difference([1, 3, 6, 7, 10, 12, 13, 17])
listChecker([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]) # 5 x 0, 7 x 1