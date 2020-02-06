# Opdracht 1
def tekenForPyramid():
    maxlen = int(input("Hoe groot? \n"))

    for line in range(0, maxlen):
        for ster in range(0, line+1):
            print("* ", end="")
        print("\r")
    tekenForPyramidR(maxlen-1)

def tekenForPyramidR(maxlen):
    for line in reversed(range(0, maxlen)):
        for ster in reversed(range(0, line+1)):
            print("* ", end="")
        print("\r")


def tekenWhilePyramid():
    max = int(input("Hoe groot? \n"))
    lengte = 1
    i = 1
    while lengte < max:
        print(lengte * "* ")
        lengte+=1
    while lengte > 0:
        print(lengte * "* ")
        lengte-=1

# Opdracht 2
def tekstCheck():
    str1 = input("Geef een string: ")
    str2 = input("Geef nog een string: ")
    if len(str1) > len(str2):
        compareString = str2
    else:
        compareString = str1
    for ind in range(len(compareString)):
        if str1[ind] != str2[ind]:
            break
        # print(str1[ind])
    print("{} in string 1, {} in string 2, op character {} is het verschil".format(str1[ind], str2[ind], ind+1))

# tekenForPyramid()
# tekenWhilePyramid()
# tekstCheck()
# test
