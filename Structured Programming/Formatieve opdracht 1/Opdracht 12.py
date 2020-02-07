# Opdracht 12
def fizzBuzz():
    for c in range(1, 101):
        if c % 3 == 0 and c % 5 == 0:
            print("FizzBuzz")
        if c % 3 == 0:
            print("Fizz")
        elif c % 5 == 0:
            print("Buzz")
        else:
            print(c)

fizzBuzz()
