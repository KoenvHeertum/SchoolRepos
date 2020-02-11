# Opdracht 5
def numberSorter(numberList):
    oldList = numberList.copy()
    newList = []
    while oldList:
        newList.append(min(oldList))
        oldList.remove(min(oldList))

print(numberSorter([1,6,2,3,6,64,3,2,5,34,23,63,28]))