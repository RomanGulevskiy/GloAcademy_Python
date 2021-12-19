num = int(input('Введите целое число или 0 для окончания последовательности: '))
positive_nums = 0
negative_nums = 0

while num != 0:
    if num > 0:
        positive_nums += 1
        num = int(input('Введите целое число или 0 для окончания последовательности: '))
    else:
        negative_nums += 1
        num = int(input('Введите целое число или 0 для окончания последовательности: '))

print(positive_nums * negative_nums)