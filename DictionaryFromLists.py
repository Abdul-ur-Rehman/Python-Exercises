def dictionaryFromLists(keys, values):

    new_dict = {}
    for i in range(len(keys)):
        new_dict[keys[i]] = values[i]

    return new_dict

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print(dictionaryFromLists(keys,values))