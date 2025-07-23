def squaredList(list):

    squaredNumbers = []
    for i in list:
        squaredNumbers.append(i*i)

    return squaredNumbers

numbers = [1, 2, 3, 4, 5, 6, 7]

print(squaredList(numbers))