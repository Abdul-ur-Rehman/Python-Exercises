def invertedTriangle(num):

    while num >= 0:
        for i in range(num):
            print("*", end=" ")
        print()
        num -= 1

invertedTriangle(10)