def removingTuplicates(my_tuple):

    indexes_list = []
    tuple2 = ()
    for i in range(len(my_tuple)):
        for j in range(i+1, len(my_tuple)):
            if my_tuple[i] == my_tuple[j]:
                indexes_list.append(j)


    for i in range(len(my_tuple)):
        if i not in indexes_list:
            tuple2 += (my_tuple[i],)

    return tuple2

my_tuple = (1, 2, 2, 3, 4, 4, 5)

print(removingTuplicates(my_tuple))