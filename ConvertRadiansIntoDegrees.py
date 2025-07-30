import math

def degrees():
    radian = float(input("Write radian value: "))
    degree = radian * (180/math.pi)
    return degree

print("{}{}".format("Degrees = ", degrees()))