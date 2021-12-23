numbers = input('Введите список чисел, разделенных пробелом: ').split()

if len(numbers) > 0:
    
    for number in numbers:
        if numbers.count(number) == 1:
            print(number, end=' ')

else:
    print('Ошибка ввода')
