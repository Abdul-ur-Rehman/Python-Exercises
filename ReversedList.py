def reverseList(list):

    length = len(list)
    reversed_list = []
    for i in range(length-1, -1, -1):

        reversed_list.append(list[i])

    return reversed_list


list = [100, 200, 300, 400, 500]
print(reverseList(list))