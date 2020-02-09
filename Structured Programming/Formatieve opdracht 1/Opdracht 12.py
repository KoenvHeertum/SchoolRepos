# Opdracht 12
def fizzBuzz():
    for c in range(1, 101):
        if c % 3 == 0 and c % 5 == 0:
            print("FizzBuzz")
        elif c % 3 == 0:
            print("Fizz")
        elif c % 5 == 0:
            print("Buzz")
        else:
            print(c)

def fizzBuzz_2():
    """Omdat ik een 2e manier bedacht tijdens het uitschrijven van de 1e"""
    for c in range(1, 101):
        String = ""
        if c % 3 == 0 or c % 5 == 0:
            if c % 3 == 0:
                String += "Fizz"
            if c % 5 == 0:
                String += "Buzz"
        else:
            String += str(c)
        print(String)

fizzBuzz()
