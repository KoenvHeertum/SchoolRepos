from termcolor import colored

"""Zwart is goede plek, wit is niet op goede plek"""
colorkey = [] # Dit is de code die geraden moet worden
kleurenDict = {"ROOD": "R", "GREEN": "G", "BLUE": "B", "YELLOW": "Y", "WHITE": "W", "MAGENTA": "M"}
# print(colored('O ', 'red'), colored('O ', 'green'), colored('O ', 'yellow'), colored('O ', 'blue'), colored('O ', 'white'), colored('O ', 'magenta'))

def intro():
    gamemode = input("Hallo, welkom bij Mastermind. Je speelt tegen een computer.\n "
          "#1. Wil je de code raden? Typ 'Raden' in.\n #2. Wil je dat de computer je code raadt? Typ 'Feedback' in.\n")
    gamemode = ''.join(gamemode.split())
    if gamemode.lower() == "raden" or gamemode.lower() == "1":
        print("raden it is")
    elif gamemode.lower() == "feedback" or gamemode.lower() == "2":
        print("feedback it is")
    else:
        print("Dat is geen goede input. Probeer opnieuw.")
        intro()

def feedbackInput():
    code = []
    print("De beschikbare kleuren zijn {}, {}, {}, {}, {} en {}.\n".format(colored("Rood", "red"),
          colored("Groen", "green"),
          colored("Blauw", "blue"),
          colored("Geel", "yellow"),
          colored("Wit", "white"),
          colored("Paars", "magenta")))
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
            print("Kleur kon niet gelezen worden. Probeer opnieuw")
            code.clear()
            break
    if len(code) != 4:
        feedbackInput()
    else:
        tempkey = code

        confirmation = input("\nJe huidige code is:\n{}\nIs dit ok?\n".format(printColorkeyString(tempkey)))
        confirmation = ''.join(confirmation.split())
        if confirmation.lower() == "yes" or confirmation.lower() == "ja" or confirmation.lower() == "j" or confirmation.lower() == "y":
            global colorkey
            colorkey = tempkey
        else:
            print("Probeer het opnieuw.")
            feedbackInput()
        return

def printColorkeyString(kleurstring):
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
    # print(string)
    return string


intro()
feedbackInput()
print("Colorkey is {}".format(colorkey))
