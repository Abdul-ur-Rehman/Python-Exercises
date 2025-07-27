class CountTracker:

    count = 0
    def __init__(self):
        CountTracker.count += 1

    def displayCount(self):
        return CountTracker.count

obj1 = CountTracker()
obj2 = CountTracker()
obj3 = CountTracker()
obj4 = CountTracker()
obj5 = CountTracker()
print(f"Total Objects created are {CountTracker.count}.")

