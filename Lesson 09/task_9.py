num = int(input('Введите натуральное число: '))

if num > 0:
    while num > 9:
        total = 0
        while num > 0:
            total += num % 10
            num = num // 10 
        num = total
    print(num)            
else:
    print('Ошибка ввода')
