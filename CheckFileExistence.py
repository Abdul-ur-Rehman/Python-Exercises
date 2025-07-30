import os
def checkFileExistence(finename):

    if os.path.exists(finename) == True:
        print("File does exist.")

filename = "sample.txt"
checkFileExistence(filename)