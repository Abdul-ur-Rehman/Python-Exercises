def get_min_max(numbers):
    minNum = min(numbers)
    maxNum = max(numbers)

    return (minNum, maxNum)




numbers = [10, 5, 20, 2, 15]
min_max_values = get_min_max(numbers)
print(f"Original numbers: {numbers}")
print(f"Minimum and maximum values: {min_max_values}")