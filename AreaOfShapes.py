class Shape:

    def area(self):
        raise NotImplemented("Area method must be implemented by the subclass.")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        area = self.height * self.width
        return area

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        area = self.length ** 2
        return area

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * (self.radius ** 2)
        return area

rectangle = Rectangle(6, 4)
square = Square(5)
circle = Circle(4.5)
print(rectangle.area())
print(square.area())
print(circle.area())