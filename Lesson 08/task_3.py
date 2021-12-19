num = int(input('Введите число: '))
num_copy = num
total = 0

if num > 0:
    while num_copy != 0:
        total += num_copy % 10
        num_copy = num_copy // 10
    if num % total == 0:
        print('YES')
    else:
        print('NO')
else:
    print('Ошибка ввода')