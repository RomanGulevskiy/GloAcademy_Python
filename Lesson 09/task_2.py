num = int(input('Введите натуральное число: '))

if num > 0:
    
    flag = 0
    for i in range(2, num // 2 + 1):
        print(num, i)
        if num % i == 0:
            flag = 1
            break

    if (flag == 0):
        print('YES')
    else:
        print('NO')
        
else:
    print('Ошибка ввода')
