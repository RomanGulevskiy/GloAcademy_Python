num = int(input('Введите номер кармана на колесе рулетки: '))

if num > 36 or num < 0:
    print('Ошибка ввода')
else:
    if num == 0:
        print('Зеленое')
    elif num >= 1 and num <= 10:
        if num % 2 == 0:
            print('Черное')
        else:
            print('Красное')
    elif num >= 11 and num <= 18:
        if num % 2 == 0:
            print('Красное')
        else:
            print('Черное')
    elif num >= 19 and num <= 28:
        if num % 2 == 0:
            print('Черное')
        else:
            print('Красное')
    elif num >= 29 and num <= 36:
        if num % 2 == 0:
            print('Красное')
        else:
            print('Черное')