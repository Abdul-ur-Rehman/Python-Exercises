def printCharactersOnEvenIndexNumber(string):
    length = len(string)
    for i in range(length):
        if i%2 == 0:
            print(string[i])

sting = "PYnative"
printCharactersOnEvenIndexNumber(sting)