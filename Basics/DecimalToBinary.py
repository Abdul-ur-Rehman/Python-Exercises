def BinaryToDecimal(number):

    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number = int(number / 2)
    return binary

print(BinaryToDecimal(1534543))