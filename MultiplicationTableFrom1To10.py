def MultiplicationTable(num):

    for i in range(1, num + 1):
        for j in range(1, num + 1):
            print(j * i, end=" ")
        print()


MultiplicationTable(10)