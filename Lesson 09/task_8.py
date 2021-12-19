num = int(input('Введите натуральное число: '))
counter = 0

if num > 0:

    for i in range(num + 1):
        j = i
        while j != 0:
            if j % 10 == 5:
                counter += 1
                j = j // 10
            else:
                j = j // 10

    print(counter)
                
else:
    print('Ошибка ввода')
