def writeToFile(filename,output):

    with open(filename, "r") as reader:
        content = reader.readlines()
        content = [line.rstrip() for line in content]
        print("Original Content ==>", content)
        reversed_content = content[::-1]
        print("Reversed Content ==>", reversed_content)

    with open(output, "w") as writer:
        for line in reversed_content:
            writer.write(line + "\n")

        print("Content is written on file.")



filename = "sample.txt"
output = "output.txt"
writeToFile(filename, output)
