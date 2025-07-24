def reversedTuple(tuple1):
    tuple2 = ()
    for i in range(len(tuple1)-1, -1, -1):
        tuple2 += (tuple1[i],)

    return tuple2

tuple1 = (10, 20, 30, 40, 50)

print("Original Tuple:", tuple1)
print("Reversed Tuple:", reversedTuple(tuple1))