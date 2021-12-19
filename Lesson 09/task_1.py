num = int(input('Введите число: '))

while num <= 100:
    if num <= 10:
        num = int(input('Введите число: '))
        continue
    print(num)
    num = int(input('Введите число: '))
