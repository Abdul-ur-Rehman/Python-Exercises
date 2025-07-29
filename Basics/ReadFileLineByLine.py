try:
    with open("sample.txt", "r") as file:

        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("File does not exist.")