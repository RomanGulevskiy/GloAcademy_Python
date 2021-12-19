num = int(input('Введите натуральное число больше и равное 10: '))
max = 0
min = 10

if num >= 10:
    while num != 0:
        if num % 10 > max:
            max = num % 10
        elif num % 10 < min:
            min = num % 10
        num = num // 10
    print('Максимальная цифра равна', max)
    print('Минимальная цифра равна', min)        
else:
    print('Ошибка ввода')