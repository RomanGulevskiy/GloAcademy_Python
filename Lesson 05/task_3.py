num = int(input('Введите шестизначный номер билета: '))
first_nums = num // 1000
second_nums = num % 1000
first_sum = first_nums // 100 + first_nums // 10 % 10 + first_nums % 10
second_sum = second_nums // 100 + second_nums // 10 % 10 + second_nums % 10

if first_sum == second_sum:
    print('Билет', num, 'счастливый')
else:
    print('Билет', num, 'не счастливый')