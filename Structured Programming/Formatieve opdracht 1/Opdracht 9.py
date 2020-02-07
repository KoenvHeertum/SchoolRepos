# Opdracht 9
def shoveBits(ch, n):
    try:
        byte = str(ch)
        print(byte)
        if len(byte) > 8:
            print("Te lang")
        for char in byte:
            if char != "1":
                if char != "0":
                    print("Dit is geen byte.")
                    break
    except:
        print("Dit is geen byte.")

    if n > 0:
        for character in range(0, n):
            """Char op eind"""
            byte = byte[+1::] + byte[0]
            print(byte)
    elif n < 0:
        for character in range(n, 0):
            """"Char op begin"""
            byte = byte[-1] + byte[:-1]
            print(byte)

shoveBits(10001000, -3)
