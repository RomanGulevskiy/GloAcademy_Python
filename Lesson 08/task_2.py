num = int(input('Введите число: '))
counter = 0

if num > 0:
    while num > 0:
        if num % 10 == 5:
            counter += 1
            num = num // 10
        else:
            num = num // 10
else:
    print('Ошибка ввода')

print(counter)