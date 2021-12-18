str = input('Введите адрес электронной почты: ')

if '@' in str and '.' in str:
    print('Корректный')
else:
    print('Некорректный')