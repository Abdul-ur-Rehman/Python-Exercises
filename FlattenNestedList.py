def flattenNestedList(list):

    flat_list =  []
    for i in list:
        for j in i:
            flat_list.append(j)

    return flat_list

list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]
print("Nested List:", list_of_lists)
print("Flat List:", flattenNestedList(list_of_lists))