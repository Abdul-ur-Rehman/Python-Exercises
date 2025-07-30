def additem(list1, specified_item):

    for i in range(len(list1)):
        if list1[i] == 6000:
            list1.append(7000)
        elif type(list1[i]) == list:
            for j in range(len(list1[i])):
                if list1[i][j] == 6000:
                    list1[i].append(7000)
                elif type(list1[i][j]) == list:
                    for k in range(len(list1[i][j])):
                        if list1[i][j][k] == 6000:
                            list1[i][j].append(7000)

    return list1




list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

print(additem(list1, 7000))
