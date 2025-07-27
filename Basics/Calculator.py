def calculator(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return  num1 -  num2
    elif operation == "x":
        return num1 * num2
    elif operation == "/":
        return  num1 / num2
    else:
        return "Invalid Operation!"

num1 = int(input("Enter num1: "))
operation = input("Enter operation: ")
num2 = int(input("Enter num: "))

print(calculator(num1,operation, num2))