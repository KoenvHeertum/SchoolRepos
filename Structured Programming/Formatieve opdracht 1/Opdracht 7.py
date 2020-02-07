# Opdracht 7
from random import randint

def randomNumber():
    try:
        rangeInput = int(input("Geef een geheel getal op. Het getal zit tussen 0 en dit getal: \n"))
        randomInt = randint(1, rangeInput)
        # print(randomInt)
        userInput = int(input("Welk getal denk je dat het is? \n"))
        while userInput != randomInt:
            if userInput > randomInt:
                print("Getal is te hoog. Probeer opnieuw")
            elif userInput < randomInt:
                print("Getal is te laag. Probeer opnieuw")
            userInput = int(input("Welk ander getal denk je dat het is? \n"))
        print("Dat is het correcte getal")

    except:
        print("Dit is geen geheel getal. Probeer opnieuw")
        randomNumber()

randomNumber()