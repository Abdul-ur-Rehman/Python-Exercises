def extendNestedList(list1, sub_list):

    for i in range(len(list1)):
        if list1[i] == "g":
            list1.extend(sub_list)
        elif type(list1[i]) == list:
            for j in range(len(list1[i])):
                if list1[i][j] == "g":
                    list1[i].extend(sub_list)
                elif type(list1[i][j]) == list:
                    for k in range(len(list1[i][j])):
                        if list1[i][j][k] == "g":
                            list1[i][j].extend(sub_list)
                        elif type(list1[i][j][k]) == list:
                            for l in range(len(list1[i][j][k])):
                                if list1[i][j][k][l] == "g":
                                    list1[i][j][k].extend(sub_list)

    return list1


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

print(extendNestedList(list1, sub_list))

