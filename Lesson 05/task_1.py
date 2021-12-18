password = input('Введите пароль: ')
password_confirmation = input('Подтвердите пароль: ')

if password == password_confirmation:
    print('Все окей!')
else:
    print('Пароли не совпадают!')
