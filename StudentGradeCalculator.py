class GradeCalculator:

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def avg(self):
        avg = sum(self.grades) / len(self.grades)
        return avg

    def grade(self):
        grade = ""
        if self.avg() >= 90:
            grade = "A"
        elif self.avg() >= 80:
            grade = "B"
        elif self.avg() >= 70:
            grade = "C"
        elif self.avg() >= 60:
            grade = "D"

        return grade


Name = "John Doe"
Grades = [92, 88, 91, 70, 55, 86, 100]
obj = GradeCalculator(Name, Grades)
print(f"Average marks in all subjects are {obj.avg()}.")
print(f"{Name} secured {obj.grade()} grade.")