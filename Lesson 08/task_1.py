num = int(input('Введите число: '))
counter = 0

if num > 0:
    while num % 2 == 0:
        counter += 1
        num = num / 2
else:
    print('Ошибка ввода')

print(counter)