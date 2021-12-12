import math

num = int(input())
last_nums = num % 1000
first = last_nums % 10
second = last_nums % 100 // 10
third = last_nums // 100
print('У числа', num, 'сумма последних трех цифр равна', first + second + third)
