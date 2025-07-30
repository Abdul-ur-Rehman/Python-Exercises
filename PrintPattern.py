def pattern(num):
    num = num + 1
    for i in range(1, num):
        for j in range(i):
            print(i, end=" ")

        print()

pattern(9)