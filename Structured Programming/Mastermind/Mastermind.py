"""Zwart is goede plek, wit is niet op goede plek"""

def intro():
    # print("Hallo, welkom bij Mastermind. Je speelt tegen een computer.\n "
    #       "Wil je de code raden? Typ 'Raden' in.\n Wil je dat de computer je code raadt? Typ 'Feedback' in.\n")
    gamemode = input("Hallo, welkom bij Mastermind. Je speelt tegen een computer.\n "
          "#1. Wil je de code raden? Typ 'Raden' in.\n #2. Wil je dat de computer je code raadt? Typ 'Feedback' in.\n")
    if gamemode.lower() == "raden" or gamemode.lower() == "1":
        print("raden it is")
    elif gamemode.lower() == "feedback" or gamemode.lower() == "2":
        print("feedback it is")
    else:
        print("Dat is geen goede input. Probeer opnieuw")
        intro()



intro()