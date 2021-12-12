import math

num = int(input())
first = num // 1000
second = num % 1000 // 100
third = num % 100 // 10
fourth = num % 10
print('У числа', num, 'максимальная цифра равна', max(first, second, third, fourth))
