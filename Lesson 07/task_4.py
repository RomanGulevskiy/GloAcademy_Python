num1 = int(input('Введите начальное число: '))
num2 = int(input('Введите конечное число: '))
for i in range(num1, num2 + 1):
    if i % 2 == 0:
        print(i)