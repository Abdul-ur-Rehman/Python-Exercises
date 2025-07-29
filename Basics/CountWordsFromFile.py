try:
    with open("sample.txt", "r") as file:
        content = file.read()
        words = content.split()
        total_words = len(words)

        print(f"File has {total_words} total words.")

except FileNotFoundError:
    print("File Not Found!")