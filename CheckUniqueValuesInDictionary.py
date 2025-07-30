def uniqueValues(myDict):

    itemsList = list(myDict.items())
    for i in range(len(itemsList)):
        for j in range(i+1, len(itemsList)):
            if itemsList[i][1] == itemsList[j][1]:
                return False

    return True



dict1 = {'a': 1, 'b': 2, 'c': 3}             # All values unique
dict2 = {'x': 10, 'y': 20, 'z': 10}          # Value 10 is duplicated
dict3 = {} # Empty dictionary (all values are vacuously unique)

print("Dict1: ", uniqueValues(dict1))
print("Dict2: ", uniqueValues(dict2))
print("Dict3: ", uniqueValues(dict3))