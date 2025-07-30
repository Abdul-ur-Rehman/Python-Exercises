def mergeLists(list1, list2):

    final_list = []
    for i in list1:
        if i%2 == 1:
            final_list.append(i)

    for i in list2:
        if i%2 == 0:
            final_list.append(i)

    return final_list





list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

print(mergeLists(list1,list2))