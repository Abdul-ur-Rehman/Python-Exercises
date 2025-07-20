def repeatCharacters(string):
    repeat = ""
    length = len(string)
    for i in range(length):
        repeat = repeat + string[i] + string[i]

    return repeat

string = "abc112##4"
print(repeatCharacters(string))