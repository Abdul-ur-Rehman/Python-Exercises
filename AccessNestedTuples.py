def accessNestedTuple(tuple1):

    for i in range(len(tuple1)):
        if tuple1[i] == 20:
            print(tuple1[i])
        elif type(tuple1[i]) == tuple:
            for j in range(len(tuple1[i])):
                if tuple1[i][j] == 20:
                    print(tuple1[i][j])
                    print(tuple1.index(20))
        elif type(tuple1[i]) == list:
            for j in range(len(tuple1[i])):
                if tuple1[i][j] == 20:
                    print("Found 20 at nested index:", i, j)
                    print(tuple1[i][j])


tuple1 = ("Orange", (5, 15, 25),[0, 5, 10, 20, 30])
accessNestedTuple(tuple1)
