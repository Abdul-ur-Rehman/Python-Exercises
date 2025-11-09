
def removingSpaces(given_str):
    return "".join(given_str.split())

given_str = "Hello World \n Test"

print(removingSpaces(given_str))