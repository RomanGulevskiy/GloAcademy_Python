numbers = input('Введите список натуральных чисел, разделенных пробелом: ').split()

if len(numbers) > 0:
    counter = 0
    for i in range(len(numbers)):
        for k in range(i + 1, len(numbers)):
            if numbers[i] == numbers[k]:
                counter += 1
    print(counter)
else:
    print('Ошибка ввода')
