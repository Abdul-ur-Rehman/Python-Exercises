def countWords(filename):
    with open(filename, "r") as file:
        content = file.read()
        words = content.split()
        total_words = len(words)

        print(f"File has {total_words} total words.")



filename = "sample.txt"
countWords(filename)

