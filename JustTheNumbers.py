def justTheNumbers(string):
    numbersOnly = ""
    for char in string:
        if char in "0123456789":
            numbersOnly += char

    return numbersOnly

string = "abc123def456ghij6789"
print(justTheNumbers(string))