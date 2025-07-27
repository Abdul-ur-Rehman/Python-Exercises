class MaxFinder:

    def __init__(self, numbers):
        self.numbers = numbers

    def maxFinder(self):
        num = max(self.numbers)
        return num

numbers = [1, 3, 2, 5, 4]
obj = MaxFinder(numbers)
print("Max Number is", obj.maxFinder())