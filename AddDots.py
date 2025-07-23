def addDots(string):
    dots = ""
    length = len(string)
    for i in range(length):
        dots = dots + string[i] + "."
    return dots[:-1]

string = "skills"
print(addDots(string))


