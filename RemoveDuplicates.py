def removeDuplicates(duplicatedList):

    duplicated_indexes = []
    for i in range(len(duplicatedList)):
        for j in range(i+1, len(duplicatedList)):
            if duplicatedList[i] == duplicatedList[j]:
                duplicated_indexes.append(j)
    duplicated_indexes.sort(reverse=True)
    #print(duplicated_indexes)
    for i in duplicated_indexes:
        del duplicatedList[i]
    return duplicatedList



list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]
print("Duplicated List:", list_with_duplicates)
print("Non-Duplicated List:",removeDuplicates(list_with_duplicates))