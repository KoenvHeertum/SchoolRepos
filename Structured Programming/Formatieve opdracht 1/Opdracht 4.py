# Opdracht 4
def palindrome(string):
    rString = string[::-1]
    if rString.lower() == string.lower():
        print("Het is een palindroom")
    else:
        print("Het is geen palindroom")

def palindrome_self(string):
    rString = ""
    for c in string:
        rString = c + rString
    if rString.lower() == string.lower():
        print("Het is een palindroom")
    else:
        print("Het is geen palindroom")


palindrome("Woord")
palindrome("Lepel")
palindrome_self("Text")
palindrome_self("Otto")
