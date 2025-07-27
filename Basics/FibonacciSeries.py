def fibonacciSeries(num1, num2, iterations):

    series = ""
    for i in range(iterations-2):
        result = str(num1 + num2)
        num1 = num2
        num2 = int(result)
        series = series + " " + result
    return series

num1 = 0
num2 = 1
print(str(num1) + " " + str(num2) + fibonacciSeries(num1, num2, 15))

