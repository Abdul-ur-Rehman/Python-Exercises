def sortDict(myDict):

    sortedDict = {}
    for key in sorted(myDict):
        sortedDict[key] = myDict[key]

    return sortedDict


my_dict = {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}

print(sortDict(my_dict))