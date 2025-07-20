def XsEqualToOs(word):
    word = word.lower()
    length = len(word)
    x_count = 0
    o_count = 0

    for i in range(length):
        if word[i] ==  "x":
            x_count += 1

        elif word[i] == "o":
            o_count += 1

    if x_count == o_count:
        return True
    else:
        return False


word = "abc "
print(XsEqualToOs(word))