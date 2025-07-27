class Calculator:


    def addition(self, num1, num2):
        sum = num1 + num2
        return sum

    def substract(self, num1, num2):
        sub = num2 - num1
        return sub

    def multipli(self, num1, num2):
        multi = num1 * num2
        return multi

    def divide(self, num1, num2):
        divide = num2 / num1
        return divide

obj = Calculator()
print("Addition:", obj.addition(10, 15))
print("Substraction:", obj.substract(15, 60))
print("Multiplication:", obj.multipli(6, 4))
print("Division:", obj.divide(4, 24))