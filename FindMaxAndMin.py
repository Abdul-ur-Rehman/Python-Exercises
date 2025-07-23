def maxNumber(data):
    maxNum = 0
    for i in data:
        if i > maxNum:
            maxNum = i
    return maxNum

def minNumber(data):

    minNum = min(data)
    return minNum

data = [8, 2, 15, 1, 9]

print("Original List: ", data)
print("Min Number: ",minNumber(data))
print("Max Number: ",maxNumber(data))