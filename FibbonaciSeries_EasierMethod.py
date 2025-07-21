def fibonacciSeries(iterations):

    num1 = 0
    num2 = 1
    for i in range(iterations):
        print(num1, end=" ")

        result = num2 + num1
        num1 = num2
        num2 = result

fibonacciSeries(15)