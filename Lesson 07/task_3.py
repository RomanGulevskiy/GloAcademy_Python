num1 = int(input('Введите начальное число: '))
num2 = int(input('Введите конечное число: '))

if num1 < num2:
    for i in range(num1, num2 + 1):
        print(i)
else:
    for i in range(num2, num1 + 1):
        print(i)    
    