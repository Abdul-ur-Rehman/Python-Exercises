def hideNumbers(creditCard):
    length = len(creditCard)
    hiddenNumbers = ""
    for digits in range(length):
        if digits < length - 4:
            hiddenNumbers += "*"
        else:
            hiddenNumbers += creditCard[digits]
    return hiddenNumbers

creditCard = "4444444444444444"
print(hideNumbers(creditCard))
