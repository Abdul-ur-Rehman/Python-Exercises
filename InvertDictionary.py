def invertDict(dict1):

    invertedDict = {}
    for i in dict1:
        invertedDict[dict1[i]] = i

    return  invertedDict



original_dict1 = {'a': 1, 'b': 2, 'c': 3}

print(invertDict(original_dict1))