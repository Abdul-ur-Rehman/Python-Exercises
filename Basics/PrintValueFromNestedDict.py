#Method1:  using type() method

def printValue(sampleDict, word):

    for key in sampleDict:
        if key == word:
            print("Method1: ", sampleDict[key])

        elif type(sampleDict[key]) == dict:
            for key2 in sampleDict[key]:
                if key2 == word:
                    print("Method1: ", sampleDict[key][key2])

                elif type(sampleDict[key][key2]) == dict:
                    for key3 in sampleDict[key][key2]:
                        if key3 == word:
                            print("Method1: ", sampleDict[key][key2][key3])

                        elif type(sampleDict[key][key2][key3]) == dict:
                            for key4 in sampleDict[key][key2][key3]:
                                if key4 == word:
                                    print("Method1: ", sampleDict[key][key2][key3][key4])

#Method2: isinstance()

def printValue2(sampleDict, word):

    for key in sampleDict:
        if key == word:
            print("Method2: ", sampleDict[key])

        elif isinstance(sampleDict[key], dict):
            for key2 in sampleDict[key]:
                if key2 == word:
                    print("Method2: ", sampleDict[key][key2])

                elif isinstance(sampleDict[key][key2], dict):
                    for key3 in sampleDict[key][key2]:
                        if key3 == word:
                            print("Method2: ", sampleDict[key][key2][key3])

                        elif isinstance(sampleDict[key][key2][key3], dict):
                            for key4 in sampleDict[key][key2][key3]:
                                if key4 == word:
                                    print("Method2: ", sampleDict[key][key2][key3][key4])


sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

word = "history"

printValue( sampleDict, word)
printValue2( sampleDict, word)


