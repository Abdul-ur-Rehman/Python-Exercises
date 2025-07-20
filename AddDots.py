def addDots(string):
    dots = ""
    legth = len(string)
    for i in range(legth):
        dots = dots + string[i] + "."
    return dots[:-1]

string = "skills"
print(addDots(string))


