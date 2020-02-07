# Opdracht 10
def Fibonacci(int):
    rij = [1, 1]
    for r in range(2, int):
        rij.append(nextNumber(rij))
    print(rij[-1])

def nextNumber(list):
    next = list[-2] + list[-1]
    return next

Fibonacci(9)