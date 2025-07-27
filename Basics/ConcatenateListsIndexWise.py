def concatenateListsIndexWise(list1, list2):

    concatenated_list = []
    for i in range(len(list1)):
        concatenated_list.append(list1[i]+list2[i])

    return concatenated_list

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

print("Concatenated List: ", concatenateListsIndexWise(list1, list2))