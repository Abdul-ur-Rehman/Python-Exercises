def sortedNumbers(list):

    temp = 0
    for i in range(len(list)):
        for j in range(i+1, len(list)):

            if list[i] > list[j]:
                temp = list[j]
                list[j] = list[i]
                list[i] = temp

    return list


numbers = [5, 2, 8, 1, 9]

print("Original List:", numbers)
print("Sorted List:", sortedNumbers(numbers))