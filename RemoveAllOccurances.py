def removeAllOccurances(list1, num):

    for i in list1:
        if i == num:
            list1.remove(i)

    return list1


list1 = [5, 20, 15, 20, 25, 50, 20]
num = 20
print(removeAllOccurances(list1, 20))