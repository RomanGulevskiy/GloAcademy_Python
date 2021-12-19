num = int(input('Введите натуральное число: '))

if num > 0:
    
    flag = 0
    while num != 0:
        if num % 10 == 1:
            flag = 1
            break
        else:
            num = num // 10

    if (flag == 1):
        print('YES')
    else:
        print('NO')
        
else:
    print('Ошибка ввода')
