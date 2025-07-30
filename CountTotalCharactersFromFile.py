def countChars(filename):

    with open(filename, "r") as file:
        content = file.read()
        words = content.split()
        count = 0
        for word in words:
            for char in word:
                count += 1

        print(count)



filename = "sample.txt"
countChars(filename)