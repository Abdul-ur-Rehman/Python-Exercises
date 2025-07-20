
def sortList(list, order):
    if order == "asc":
        total_elements = len(list)

        for i in range(total_elements - 1):
            min_index = i

            for j in range (i + 1, total_elements):
                if list[j] < list[min_index]:
                    min_index = j

            list[i], list[min_index] = list[min_index], list[i]

    elif order == "desc":
        total_elements = len(list)

        for i in range(total_elements - 1 ):
            min_index = i

            for j in range(i + 1, total_elements):
                if list[j] > list[min_index]:
                    min_index = j

            list[i], list[min_index] = list[min_index], list[i]

    elif order == "none":
        return list



list = [2,4,8.5,0.7,1,9,5.5]
order = input("Write order of sorting(Hint: asc, desc, none): ")
print("{}{}".format("Original List:", list))
sortList(list, order)
print("{}{}".format("Sorted List:", list))


