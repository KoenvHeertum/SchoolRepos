import random
from termcolor import colored
""""termcolor gebaseerd op https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python"""

"""Zwart is goede plek, wit is niet op goede plek"""
colorkey = [] # Dit is de code die geraden moet worden
kleurenList = ["r", "g", "b", "y", "w", "p"] # dit is een lijst met alle kleuren
# print(colored('O ', 'red'), colored('O ', 'green'), colored('O ', 'yellow'), colored('O ', 'blue'), colored('O ', 'white'), colored('O ', 'magenta'))

def intro():
    print("-" * 80)
    gamemode = input("Hallo, welkom bij Mastermind. Je speelt tegen een computer.\n "
          "#1. Wil je de code raden? Typ 'Raden' in.\n #2. Wil je dat de computer je code raadt? Typ 'Feedback' in.\n")
    print("-" * 80)
    gamemode = ''.join(gamemode.split())
    if gamemode.lower() == "raden" or gamemode.lower() == "1":
        radenGameloop()
    elif gamemode.lower() == "feedback" or gamemode.lower() == "2":
        feedbackGameloop()
    else:
        print("Dat is geen goede input. Probeer opnieuw.")
        intro()

def createColorkey():
    """Je vult de colorkey in, aan de hand van 4 vragen. Na afloop krijg je de vraag of je akkoord gaat met je code."""
    code = []
    print("De beschikbare kleuren zijn {}, {}, {}, {}, {} en {}.".format(colored("Rood", "red"),
          colored("Groen", "green"),
          colored("Blauw", "blue"),
          colored("Geel", "yellow"),
          colored("Wit", "white"),
          colored("Paars", "magenta")))
    print("-" * 80)
    for i in range(1,5):
        color = input("Voer hier kleur {} in: \n".format(i))
        color = ''.join(color.split())
        if color.lower() == "r" or color.lower() == "rood" or color.lower() == "red":
            code.append("r")
        elif color.lower() == "b" or color.lower() == "blauw" or color.lower() == "blue":
            code.append("b")
        elif color.lower() == "y" or color.lower() == "geel" or color.lower() == "yellow":
            code.append("y")
        elif color.lower() == "g" or color.lower() == "groen" or color.lower() == "green":
            code.append("g")
        elif color.lower() == "w" or color.lower() == "white" or color.lower() == "wit":
            code.append("w")
        elif color.lower() == "p" or color.lower() == "paars" or color.lower() == "purple":
            code.append("p")
        else:
            print("Kleur kon niet gelezen worden. Herstart het programma en probeer opnieuw")
            exit(401) #Ik moet hier restarten omdat hij anders de oude code ook blijft lezen. Dit crasht het programma.
    print("-" * 80)
    if len(code) != 4:
        print(code)
        print("Failswitch: Code bestaat NIET uit 4 chars.")
        createColorkey()
    else:
        tempkey = code

        confirmation = input("Je huidige code is:\n{}\nIs dit ok?\n".format(printColorkeyString(tempkey)))
        confirmation = ''.join(confirmation.split())
        if confirmation.lower() == "yes" or confirmation.lower() == "ja" or confirmation.lower() == "j" \
                or confirmation.lower() == "y" or confirmation.lower() == "ok":
            return tempkey
        else:
            print("Probeer het opnieuw.")
            createColorkey()


def createCombinationList():
    """Maakt alle 1296 mogelijke combo's aan"""
    cList = kleurenList.copy()
    cList2 = cList.copy()
    cList3 = cList.copy()
    cList4 = cList.copy()
    allCombinations = []
    for i in cList:
        for j in cList2:
            for k in cList3:
                for l in cList4:
                    allCombinations.append([i, j, k, l])
    return allCombinations


def generateColorstring():
    """Computer genereert colorstring en returned target"""
    string = []
    for i in range(1, 5):
        string.append(random.choice(kleurenList))
    return string

def generateFeedback(kleurstring, key):
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

def generateFirstTurn():
    """Genereert de eerste turn, dat een volgorde van AABB volgt"""
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

# Source voor korte versie: https://www.w3schools.com/python/python_howto_remove_duplicates.asp
def kleurenInCombo(combo):
    """Returned lijst met de kleuren van een gok, zonder duplicates"""
    kleuren = list(dict.fromkeys(combo))
    return kleuren


def printFeedback(zwart, wit):
    print("-" * 80)
    print("Feedback: {} zwarte pinnen, {} witte pinnen.".format(zwart, wit))
    if zwart == 4:
        print("Gefeliciteerd, je hebt de code gekraakt!")
    print("-" * 80)

def printColorkeyString(kleurstring):
    """Zet een list om in een rij pinnen (in kleur)"""
    string = ""
    for i in kleurstring:
        if i == "r":
            string += (colored('O ', 'red'))
        elif i == "b":
            string += (colored('O ', 'blue'))
        elif i == "g":
            string += (colored('O ', 'green'))
        elif i == "y":
            string += (colored('O ', 'yellow'))
        elif i == "w":
            string += (colored('O ', "white"))
        elif i == "p":
            string += (colored('O ', 'magenta'))
        else:
            print("ERROR: colorkey bestaat niet uit 4 juiste kleuren.")
    return string

def radenGameloop():
    """Gameloop als JIJ de code wilt raden"""
    global colorkey
    colorkey = generateColorstring()
    beurten = 10
    for i in range(1, beurten+1):
        print("Turn #{} (van {})".format(i, beurten))
        laatsteZet = createColorkey()
        zwart, wit = generateFeedback(laatsteZet, colorkey)
        printFeedback(zwart, wit)
        if zwart == 4:
            break
    print("De code was: {}".format(printColorkeyString(colorkey)))


def feedbackGameloop():
    """Gameloop als de computer jouw code moet raden"""
    """Deze code is een beetje een chaos, maar heb expres niet te veel functies aangemaakt omdat 
        je anders heel veel moet doorgeven bij elke functie"""
    global colorkey
    colorkey = createColorkey()
    allCombinations = createCombinationList()
    # latestTurnCombo = generateColorstring()
    latestTurnCombo = generateFirstTurn()
    beurten = 10
    print("-" * 80)
    for i in range(1, beurten+1):
        print("\n\n" + "-" * 80)
        print("Turn #{} (van {})".format(i, beurten))
        print("allcombo lengte: {}".format(len(allCombinations)))
        print("-" * 80)
        print("Computer's gok: \n{}\n{}".format(printColorkeyString(latestTurnCombo), latestTurnCombo))
        zwart, wit = generateFeedback(latestTurnCombo, colorkey)
        printFeedback(zwart, wit)
        if zwart == 0 and wit == 0:
            kleuren = kleurenInCombo(latestTurnCombo)
            for kleur in kleuren:
                for aItems in allCombinations:    #1296
                    if kleur in aItems:
                        allCombinations.remove(aItems)
        if zwart == 4:
            print("CPU heeft de code geraden.")
            break
        for j in allCombinations:
            zwartCombo, witCombo = generateFeedback(j, latestTurnCombo)
            if zwartCombo != zwart or witCombo != wit:
                allCombinations.remove(j)
        latestTurnCombo = allCombinations[allCombinations.index(random.choice(allCombinations))]
        # input("hier input voor als je turn voor turn wilt doen.")

    print("De code was: {}".format(printColorkeyString(colorkey)))



intro()

