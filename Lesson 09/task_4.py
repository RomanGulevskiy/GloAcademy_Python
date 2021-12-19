num = int(input('Введите натуральное число: '))

if num > 0:
    
    for i in range(1, num + 1):
        if i in range(2, 9) or i in range(128, 257) or i in range(1024, 2049):
            continue
        print(i)

else:
    print('Ошибка ввода')
