#Method1: Loop

def initializeDict(employees, defaults):

    newDict = {}
    for i in employees:
        newDict[i] = defaults

    return newDict

#Method2: fromkeys()

def initializeDict2(employees, defaults):

    return dict.fromkeys(employees, defaults)

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

print("Method1:", initializeDict(employees, defaults))
print("Method2:", initializeDict2(employees, defaults))