def removeCharacters(string, n):

    length = len(string)
    if n >= length:
        print("Sorry! You cannot slice the complete string.")
    else:
        print(string[n:length])

string = "pynative"

removeCharacters(string, 10)
