class StudentResult():

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def sumOfMarks(self):
        return sum(self.marks)

    def avgMarks(self):
        return self.sumOfMarks() / len(self.marks)

    def dispalyResult(self):
        return f"Name: {self.name}, Total Marks: {self.sumOfMarks()}, Average Marks: {self.avgMarks()}"

obj1 = StudentResult("Bob", [76, 84, 90])
obj2 = StudentResult("Anna", [67, 99, 55])
obj3 = StudentResult("Mark", [73, 77, 80])

print(obj1.dispalyResult())
print(obj2.dispalyResult())
print(obj3.dispalyResult())