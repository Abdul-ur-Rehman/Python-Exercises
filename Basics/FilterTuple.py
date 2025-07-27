def filterTuple(students):

    list1 = []
    for i in students:
        if i[1] < 90:
            list1.append(i)

    return list1

students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

print(filterTuple(students))