def countSpecificWord(filename, given_word):

    with open(filename, "r") as file:
        content = file.read().upper()
        words = content.split()
        count = 0
        for word in words:
            if word == given_word:
                count += 1
        print(count)

filename = "sample.txt"
given_word = "QA"
countSpecificWord(filename, given_word)