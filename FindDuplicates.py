
def findDuplicates(duplicated_list):
    duplicate_elements = []
    for num in range(len(duplicated_list)-1):
        for num2 in range(num+1,len(duplicated_list)):
            if duplicated_list[num] == duplicated_list[num2]:
                duplicate_elements.append(duplicated_list[num])

    return duplicate_elements


duplicated_list = [1, 2, 3, 2, 4, 5, 1,6,8,3,6,9,9]
print(len(duplicated_list))

print(findDuplicates(duplicated_list))