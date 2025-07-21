def sumOfCurrentAndPreviousNumbers(firstNum, lastNum):
    currentNum = 0
    previousNum = 0

    print(f"Printing current and previous number sum in a range({lastNum})")
    for i in range(lastNum):
        print(f"Current Number {currentNum} Previous Number  {previousNum}  Sum: ", currentNum + previousNum)
        previousNum = currentNum
        currentNum = i+1

sumOfCurrentAndPreviousNumbers(1, 10)