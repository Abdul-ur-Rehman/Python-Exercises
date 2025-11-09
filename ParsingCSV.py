import csv

with open("test_csv.csv","r") as file:

    data = []
    reader = csv.DictReader(file)
    data = list(reader)

print(data)
print(reader)