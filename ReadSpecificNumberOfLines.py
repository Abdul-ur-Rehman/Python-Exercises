try:
    with open("sample.txt", "r") as file:

        for i in range(5):
            print(file.readline().strip())

except FileNotFoundError:
    print("File Not Found!")

