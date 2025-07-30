#Method 1
class DigitInWords:

    def __init__(self, number):
        self.number = number

    def findDigit(self):
        digit = self.number % 10
        return digit

    def digitInWords(self):
        Word = ""
        if self.findDigit() == 0:
            Word = "Zero"
        elif self.findDigit() == 1:
            Word = "One"
        elif self.findDigit() == 2:
            Word = "Two"
        elif self.findDigit() == 3:
            Word = "Three"
        elif self.findDigit() == 4:
            Word = "Four"
        elif self.findDigit() == 5:
            Word = "Five"
        elif self.findDigit() == 6:
            Word = "Six"
        elif self.findDigit() == 7:
            Word = "Seven"
        elif self.findDigit() == 8:
            Word = "Eight"
        elif self.findDigit() == 9:
            Word = "Nine"
        return Word

#Method 2
class DigitInWords2:
    def digitInWords(self, number):
        last_digit = number % 10
        numbers = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        return numbers[last_digit]

obj = DigitInWords(2387462834)
obj2 = DigitInWords2()
print(f"Method 1 ==> Last digit is {obj.digitInWords()}.")
print(f"Method 2 ==> Last digit is {obj2.digitInWords(2387462834)}.")
