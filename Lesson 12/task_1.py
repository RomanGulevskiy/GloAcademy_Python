def calc_number_ranks(number_1, number_2):
    total_1 = 0
    total_2 = 0
    if number_1 > 0 and number_2 > 0:
        while number_1 != 0:
            total_1 += 1
            number_1 = number_1 // 10
        while number_2 != 0:
            total_2 += 1
            number_2 = number_2 // 10
        return total_1 * total_2
    else:
        print('Ошибка ввода')

number_1 = int(input('Введите натуральное число: '))
number_2 = int(input('Введите натуральное число: '))
print(calc_number_ranks(number_1, number_2))