def print_month_days(month):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        return 28
    else:
        return 31

month = int(input('Введите номер месяца: '))
if month > 0 and month < 13:
    print(print_month_days(month))
else:
    print('Ошибка ввода')