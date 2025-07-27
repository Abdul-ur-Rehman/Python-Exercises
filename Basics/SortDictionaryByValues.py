def sortDict(myDict):

    itemsList = list(my_dict.items())
    for i in range(len(itemsList)):
        for j in range(i+1, len(itemsList)):
            if itemsList[i][1] > itemsList[j][1]:
                itemsList[i], itemsList[j] = itemsList[j], itemsList[i]


    return dict(itemsList)

my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}

print(sortDict(my_dict))
