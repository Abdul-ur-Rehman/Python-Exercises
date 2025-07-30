def removeEmptyString(list):

    count = 0
    new_list = list.copy()
    for i in range(len(list)):
        if list[i] == "":
            count += 1
            del new_list[i]

    print("Total Empty Strings:", count)
    return new_list


list = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print("Original List:",list)

print("Modified List:", removeEmptyString(list))