# Opdracht 3
def count(list):
    numberdict = {}
    for number in list:
        if number in numberdict:
            numberdict[number] += 1
        else:
            numberdict[number] = 1
    print(numberdict)

count([1, 1, 2, 2, 2, 3, 4, 5, 5, 5, 6])