import os
def checkFileExistence(finename):

    if os.path.exists(finename) == True:
        print("File does exist.")

    fileSize = os.path.getsize(filename)
    print(f"File size is {fileSize} bytes.")

filename = "sample.txt"
checkFileExistence(filename)