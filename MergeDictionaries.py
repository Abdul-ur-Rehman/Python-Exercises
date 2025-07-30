#Method1
def mergeDictionaries1(dict1, dict2):

    for keys, values in dict2.items():
        dict1[keys] = values

    return dict1
#Method2
def mergeDictionaries2(dict1, dict2):
    dict3 = dict1.copy()
    dict3.update(dict2)

    return dict3

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

print(mergeDictionaries1(dict1, dict2))
print(mergeDictionaries2(dict1, dict2))