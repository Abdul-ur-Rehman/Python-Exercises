def countFrequencies(string1):

    dict = {}
    for char in string1:
        dict[char] = dict.get(char, 0) +1

    return dict

string1 = 'mississippi'
print(countFrequencies(string1))

