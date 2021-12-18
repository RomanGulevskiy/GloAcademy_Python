numbers = int(input('Введите количество чисел: '))
flag = 0

for i in range(1, numbers + 1):
    user_number = int(input('Введите число: '))
    if user_number % 2 != 0:
        flag = 1

if flag == 1:
    print('YES')
else:
    print('NO')