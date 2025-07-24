def concatenateElementsOfLists(list1, list2):

    concatenated_Elements = []
    for i in list1:
        for j in list2:
            concatenated_Elements.append(i+j)

    return concatenated_Elements

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

print("Concatenated Elements:", concatenateElementsOfLists(list1, list2))