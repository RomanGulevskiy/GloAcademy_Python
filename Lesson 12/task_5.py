def is_magic_date(date):
    date = date.split('.')
    day = date[0]
    month = date[1]
    year = date[2]

    if day.isdigit() and month.isdigit() and year.isdigit():        
        if int(day) > 31 or int(day) < 1:
            return 'Ошибка ввода'
        elif int(month) > 12 and int(month) < 1:
            return 'Ошибка ввода'
        elif not len(year) == 4:
            return 'Ошибка ввода'
        else:
            return int(day) * int(month) == int(year[2:4])

date = input('Введите дату: ')
print(is_magic_date(date))
