# Opdracht 11
def convert():
    String = input("Geef een String: ")
    # [ord(c) for c in String]
    bytesList = list(bytes(b'String'))
    print(bytesList)

""" Ik kom niet goed uit deze opdracht, maar volgens mij moet ik de String naar bytes omzetten en dan +input doen op de unicode van deze bytes.
Hierdoor krijg je dan als het goed is die nieuwe letters, en deze zet je terug om in een String die je print. """

convert()
