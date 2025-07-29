def appendToFile(output, new_line):

    with open(output, "a") as writer:
        writer.write( new_line + "\n")

    print("New line is appended in the output.txt file.")

output = "output.txt"
new_line = "This is an appended line."
appendToFile(output, new_line)