surname = input('Введите фамилию: ')
name = input('Введите имя: ')
patronymic = input('Введите отчество: ')

if surname.isalpha() and name.isalpha() and patronymic.isalpha:
    print(surname, ' ', name[0], '.', patronymic[0], '.', sep = '')
else:
    print('Ошибка ввода')
