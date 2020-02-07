# Opdracht 6
def averageCounter(list):
    total = 0
    for i in list:
        total += i
    average = total/len(list)
    return average


def averageCounterLists(list):
    total = 0
    for sublist in list:
        for i in sublist:
            total += i
    average = total / len(list)
    return average


averageCounter([1, 2, 3, 4, 5, 6, 7, 8, 9])
averageCounterLists([[1, 2], [3, 4], [5, 6], [7, 8, 9]])
