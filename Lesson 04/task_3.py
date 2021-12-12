num = int(input())
first = num // 100
second = num // 10 % 10
third = num % 10
print('Сумма цифр числа', num, 'равна', first + second + third)
print('Произведение цифр числа', num, 'равна', first * second * third)
